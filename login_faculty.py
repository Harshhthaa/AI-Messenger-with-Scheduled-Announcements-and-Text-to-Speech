import mysql.connector as mc

db = mc.connect(host="localhost",username="root",passwd="1234",database="radio")
cur = db.cursor()
print('connected to db')

cur.execute("select * from faculty_confirmation")
u = cur.fetchall()

def login(fac_id):
    flag = False
    for i in u:
        if fac_id == i[2]:
            a = i
            flag = True
            break
    if flag==True:
        print('got it',a[2])
    else:
        print("not your day bye bye")
        

v = 1093
login(v)
