'''
Created on 2014-5-25

@author: KEVIN
'''
#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");
conn.execute("INSERT INTO USER (ID,NICKNAME,EMAIL,ROLE) VALUES (1,'dkrose.random','dkrose.random@gmail.com',0)");
conn.commit()