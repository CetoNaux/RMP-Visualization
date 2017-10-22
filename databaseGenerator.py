import sqlite3
from sqlite3 import Error
import data
import parser
import sqlite3

if __name__ == '__main__':
    count = 0
    readfile = open('osuRate.txt', 'r')

    connection = sqlite3.connect("professors.db")
    cursor = connection.cursor()
    sql_command = """CREATE TABLE professors(department, first, last, score, numberRates)"""
    cursor.execute(sql_command)
    readlines = readfile.readlines()
    for line in readlines:
            Type = line.split(",")
            d = Type[0]
            f = Type[1]
            l = Type[2]
            s = Type[3]
            r = int((Type[4].split(" "))[0])
            if (s!='N/A'):
                s=float(s)
                collection = [d,f,l,s,r]
                cursor.executemany('insert into professors values (?,?,?,?,?)',(collection,))

                connection.commit()
    connection.close()
    print("lihuisb")
