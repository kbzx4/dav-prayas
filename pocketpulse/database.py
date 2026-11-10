import mysql.connector
DB_CONFIG = {
    "host":"localhost",
    "user":"root",
    "password":"726705@12",
    "database":"prayas"
}
def get_transactions():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    qry = "select * from transactions"
    cursor.execute(qry)
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return transactions 
def add(title,amount,category,date,type):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    qry = "insert into transactions(title,amount,category, t_date,type) values (%s,%s,%s,%s,%s)"
    values = (title,amount,category,date,type)
    cursor.execute(qry,values)
    conn.commit()
    cursor.close()
    conn.close()
