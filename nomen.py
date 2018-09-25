# -*- coding: utf-8 -*-

import io
import sys
import os
import sqlite3
import pyperclip
import time
dict = sqlite3.connect('/Users/oshino/Applications/DicGerman/dicgerman.db')
#enc_source = enc_target = 'utf-8'
nfile = '/Users/oshino/Applications/DicGerman/nomen/nomen.txt'
if len(sys.argv) == 2:
    nfile = sys.argv[1]

sql = "SELECT * FROM nomen WHERE wortart='Substantiv' and \
lemma='{}'".decode('utf8')
sql_pl = "SELECT * FROM nomen WHERE wortart='Substantiv' and \
\"nominativ plural\"='{}'".decode('utf8')
sql_pl1 = "SELECT * FROM nomen WHERE wortart='Substantiv' and \
\"nominativ plural 1\"='{}'".decode('utf8')
#read wordlist from clipboard oder from nfile
clip = pyperclip.paste()
wordlist = clip.split('\n')
# if len(clip) > 10:
#     wordlist = clip.split('\n')
# else:
#     with open(nfile, 'r') as f:
#         wordlist = f.read().decode('utf8').split('\n')
#         wordlist.pop()
#result destination
w = open('/Users/oshino/Applications/DicGerman/nomen/result.txt', 'w')

#query and write file once a word
for word in wordlist:
    #query
    cursor = dict.execute(sql.format(word))
    rows = cursor.fetchall()
    #re_query if query_result is blank
    if len(rows) == 0:
        cursor = dict.execute(sql_pl.format(word))
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor = dict.execute(sql_pl1.format(word))
            rows = cursor.fetchall()
            if len(rows) == 0:
                rows = [['-']*76]
                rows[0][0] = word
    #write query result
    w.write(u"{}\t".format(rows[0][0]).encode('utf8'))#lemma
    if rows[0][3] == None:
        w.write(u'pl\t')#genus when plural
    else:
        w.write(u"{}\t".format(rows[0][3]).encode('utf8'))#genus
    if rows[0][13] != None:
        w.write(u'{}\n'.format(rows[0][13]).encode('utf8'))#nominativ plural
    elif rows[0][15] != None:
        w.write(u'{}\n'.format(rows[0][15]).encode('utf8'))#nominativ plural 1
    else:
        w.write(u'-\n'.encode('utf8'))#line break

# w = open('nomen/result.txt', 'w')
# for row in cursor:
#     w.write(u"{}\t{}\t{}\n".format(row[0],row[1],row[2]).encode('utf8')\
#     .replace('None','-'))
