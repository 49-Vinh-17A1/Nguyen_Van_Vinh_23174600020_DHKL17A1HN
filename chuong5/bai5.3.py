import sqlite3
conn = sqlite3.connect(r'C:\code\gitpythonnangcao\baitap pỵthon\chuong5\data5.3.db')
curso = conn.cursor()
curso.execute("""CREATE TABLE IF NOT EXISTS nhanvien(
              id INTEGER PRIMARYKEY,
              "Ten" Text,
              "Tuoi" INTEGER)""")
conn.commit()
conn.close()