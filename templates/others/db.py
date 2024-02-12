import pymysql

timeout = 30
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="DJP",
    host="mysql-djp-dotjp-24.a.aivencloud.com",
    password="AVNS_ZwVMvOQDIL0KyOm3gIH",
    read_timeout=timeout,
    port=26193,
    user="avnadmin",
    write_timeout=timeout,
)

try:
  cursor = connection.cursor()
  # cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
  # cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
  cursor.execute("SELECT * FROM jobs")
  print(cursor.fetchall())
finally:
  connection.close()
