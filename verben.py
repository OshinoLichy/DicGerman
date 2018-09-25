# -*- coding: utf-8 -*-

import io
import sys
import os
import sqlite3
import pyperclip
import time
dict = sqlite3.connect('/Users/oshino/Applications/DicGerman/dicgerman.db')
#enc_source = enc_target = 'utf-8'
vfile = '/Users/oshino/Applications/DicGerman/verben/source.txt'
if len(sys.argv) == 2:
    vfile = sys.argv[1]

sql = "SELECT * FROM verben WHERE Infinitive='{}'".decode('utf8')
sql_scd = "SELECT * FROM verben WHERE \"Präsens_du\"='{}'".decode('utf8')
sql_thrd = "SELECT * FROM verben WHERE \"Präsens_er, sie, es\"='{}'".decode('utf8')
sql_ptzp = "SELECT * FROM verben WHERE \"Partizip II\"='{}'".decode('utf8')

#read wordlist from clipboard oder from vfile
clip = pyperclip.paste()
wordlist = clip.split('\n')
# if len(clip) > 10:
#     wordlist = clip.split('\n')
# else:
#     with open(vfile, 'r') as f:
#         wordlist = f.read().decode('utf8').split('\n')
#         wordlist.pop()
#result destination
w = open('/Users/oshino/Applications/DicGerman/verben/result.txt', 'w')

#query and write file once a word
for word in wordlist:
    #query
    cursor = dict.execute(sql.format(word))
    rows = cursor.fetchall()
    #re_query if query_result is blank
    if len(rows) == 0:
        cursor = dict.execute(sql_thrd.format(word))
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor = dict.execute(sql_ptzp.format(word))
            rows = cursor.fetchall()
            if len(rows) == 0:
                cursor = dict.execute(sql_scd.format(word))
                rows = cursor.fetchall()
                if len(rows) == 0:
                    rows = [['-']*10]
                    rows[0][0] = word
    # w.write(u"{}\t".format(rows[0][0]).encode('utf8'))
    # if rows[0][3] == None:
    #     w.write(u'pl\t')
    # else:
    #     w.write(u"{}\t".format(rows[0][3]).encode('utf8'))
    # if rows[0][13] != None:
    #     w.write(u'{}\n'.format(rows[0][13]).encode('utf8'))
    # elif rows[0][15] != None:
    #     w.write(u'{}\n'.format(rows[0][15]).encode('utf8'))
    # else:
    #     w.write(u'-\n'.encode('utf8'))

    #write query result
    for i in range(10):
        if rows[0][i] == None:
            rows[0][i] = '-'
    w.write(u"{}\t{} {}\t{}\n"\
    .format(rows[0][0],rows[0][9],rows[0][5],rows[0][3]).encode('utf8'))\
    #Infinitive, Hilfsverb, Partizip II, Präsens_er, sie, es
# with open('verben/result.txt','r') as f:
#     pyperclip.copy(f.read().decode('utf8'))
#

# w = open('nomen/result.txt', 'w')
# for row in cursor:
#     w.write(u"{}\t{}\t{}\n".format(row[0],row[1],row[2]).encode('utf8')\
#     .replace('None','-'))
