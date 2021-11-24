import sqlite3
from Shopping import Shopping

con = sqlite3.connect('C:/itay/sqlite/mydb2.db')
cur = con.cursor()

cur.execute("select * from shopping")

for row in enumerate(cur):
    print(row)

def add_item(cur, table, id, name, amount, maavar):
    cur.execute(f'INSERT INTO {table} VALUES ({id}, "{name}",'\
                f' {amount}, {maavar})')

def add_shopping(cur, item):
    cur.execute(f'INSERT INTO shopping VALUES ({item.id}, "{item.name}",'\
                f' {item.amount}, {item.maavar})')

#pepper = Shopping(9, 'pepper', 20, 5)
#add_shopping(cur, pepper)

#cur.execute("INSERT INTO shopping VALUES (8, 'humus', 12, 7)")
add_item(cur, "shopping", 8, 'humus', 12, 7)

cur.execute("UPDATE shopping SET amount=14"\
            " WHERE name = 'humus'")

cur.execute("DELETE FROM shopping "\
            " WHERE name = 'humus'")

con.commit();

cur.execute("select * from shopping")

_lst1 = []
for row in cur:
    print(row)
    _lst1.append(Shopping(row[0], row[1], row[2], row[3]))
print(_lst1)

cur.execute("select * from shopping")
_lst2 = [Shopping(row[0], row[1], row[2], row[3]) for row in cur]
print(_lst2)

con.close()
