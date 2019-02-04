# -*- coding: utf-8 -*-
"""
This is a small python library that helps you a little with simple sqlite3 tasks.
Its a little bit generic, so you can adapt it to your own necessities. 
All functions open, modify commit and close the database so you dont  have to bother about it.
"""

import sqlite3


"""
Transforms dictionaries in strings
Input: dictionary.
Output: string: key item, key2 item2, ...
"""
def dictostring (dictionary):
    return ', '.join("{!s} {!s}".format(key,val) for (key,val) in dictionary.items())

"""
    This funcion creates a table in .JB file.
    If the .JB file not exists, creates a new one.
    If the table already exists, it does nothing.
    INPUT: File name, table name, dictionary with rows configuaration (see example down low)
"""    
    
def create (filename, tablename, rows):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()
    tabletext = dictostring (rows)
    command = "CREATE TABLE if NOT EXISTS %s (%s)" % (tablename, tabletext)
    cur.execute(command)
    conn.commit()
    conn.close()
    
"""
    Turns list to a formated string.
    Created to be used in insert function.
    INPUT: List with 
"""
def listtostring(list1):
    return ', '.join("{!s}".format(key) for key in list1)
    
    

def insert (filename, tablename, values):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()
    valuesstr = listtostring(values)
    command = "INSERT INTO %s VALUES(%s)" % (tablename, valuesstr)
    cur.execute(command)
    conn.commit()
    conn.close()
    
    
def view (filename, tablename):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()
    command = "SELECT * FROM %s" % (tablename)
    cur.execute(command)
    rows = cur.fetchall()
    conn.close()
    return rows

def delete (filename, tablename, category, obj):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()
    command = "DELETE FROM %s WHERE %s = %s" % (tablename, category, obj)
    cur.execute(command)
    conn.commit()
    conn.close()

def update(filename, tablename, categoriesList, objList, tupl ):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()
    liststr = (', '.join("{!s}={!s}".format(key1, key2) for (key1, key2) in zip(categoriesList, objList)))
    command = "UPDATE %s SET %s WHERE %s = %s" % (tablename, liststr, tupl[0], tupl[1])
    cur.execute(command)
    conn.commit()
    conn.close()

#examples to use:
## main:
#filename= "lite.db"
#tablename = "store"
#rows = {
#        "item" : "TEXT",
#        "quantity" : "INTEGER",
#        "price" : "REAL"
#        }
#
#values = ["'banana chiquita'", 1, 1.5] # the values to  be inserted in the table. in the example ['name', quantity, price]
#create(filename, tablename, rows)
#insert(filename, tablename, values)
#delete("item", "'banana chiquita'")
#update(filename, tablename, ["quantity", "price"], [12, 2.5], ("item", "'banana chiquita'" ))
#print (view(filename, tablename))
