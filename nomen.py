# -*- coding: utf-8 -*-

import io
import sys
import sqlite3
dict = sqlite3.connect('dicgerman.db')
#enc_source = enc_target = 'utf-8'
vfile = 'verben/verben.txt'
nfile = 'nomen/nomen.txt'

sql = "SELECT * FROM nomen WHERE wortart='Substantiv' and \
lemma='{}'".decode('utf8')
with open('nomen/nomen.txt', 'r') as f:
    wordlist = f.read().decode('utf8').split('\n')
    wordlist.pop()
w = open('nomen/result.txt', 'w')
for word in wordlist:
    cursor = dict.execute(sql.format(word))

    rows = cursor.fetchall()
    if len(rows) == 0:
         rows = [['-']*76]
    w.write(u"{}\t".format(rows[0][0]).encode('utf8'))
    if rows[0][3] == None:
        w.write(u'pl\t')
    else:
        w.write(u"{}\t".format(rows[0][3]).encode('utf8'))
    if rows[0][13] != None:
        w.write(u'{}\n'.format(rows[0][13]).encode('utf8'))
    elif rows[0][15] != None:
        w.write(u'{}\n'.format(rows[0][15]).encode('utf8'))
    else:
        w.write(u'-\n'.encode('utf8'))

# w = open('nomen/result.txt', 'w')
# for row in cursor:
#     w.write(u"{}\t{}\t{}\n".format(row[0],row[1],row[2]).encode('utf8')\
#     .replace('None','-'))
