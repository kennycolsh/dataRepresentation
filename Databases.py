import mysql.connector

db = mysql.connector.connect(
    host ="localhost", user="root",
    password="",database="popcars"
)



cursor = db.cursor()
sql="insert into cars (reg,make,model,price,totalvotes) values (%s,%s,%s,%s,%s)"
values = ("121C1547","AUDI","A4",12501, 4)
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)