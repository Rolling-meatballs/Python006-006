import pymysql

HOST = 'localhost'
PASSWORD = '123456'
USER = 'root'
PORT = 3306
NAME = 'ji_ke'

db = pymysql.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    db=NAME,
)

try:
    with db.cursor() as cursor:
        sql = '''SELECT VERSION'''
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f'fetch error {e}')

finally:
    db.close()

print(f'Database version : {result}')
