# -*- coding: utf-8 -*-

import io
import sys
import sqlite3
dict = sqlite3.connect('dicgerman.db')
#enc_source = enc_target = 'utf-8'
vfile = 'verben/verben.txt'
nfile = 'nomen/nomen.txt'

sql = "SELECT * FROM gpnomen WHERE lemma IN ('{}')".decode('utf8')
with open('nomen/nomen.txt', 'r') as f:
    wordlist = f.read().decode('utf8').split('\n')
    wordlist.pop()
cursor = dict.execute(sql.format("', '".join(wordlist)))

w = open('nomen/result.txt', 'w')
for row in cursor:
    w.write(u"{}\t{}\t{}\n".format(row[0],row[1],row[2]).encode('utf8')\
    .replace('None','-'))
