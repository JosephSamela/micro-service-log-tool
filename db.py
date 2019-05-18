import sqlite3
from sqlite3 import Error

class db:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite')

    def db_query(self, query='SELECT * FROM logs'):
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def db_insert(self, log):
        cur = self.conn.cursor()
        s = log['source']
        c = log['code']
        t = log['type']
        d = log['description']
        cur.execute('INSERT INTO logs(source,code,type,description) VALUES("{}",{},"{}","{}")'.format(s,c,t,d))
        return self.conn.commit()

if __name__ == "__main__":
    db().db_insert({"source":"Customer Information Service","code":1255,"type":"Information","description":"example"})
