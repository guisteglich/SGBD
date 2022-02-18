import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="gui",
                                  password="geromito1903",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="empresa")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

ProjNum = 1
Dnum = 50
ProjLocal = 200

for i in range(1, ProjLocal+1):
    print("departamento:", i)
    for j in range(1, Dnum+1):
        print("PROJETO: ", ProjNum)
        sql = "INSERT INTO PROJETO (Projnumero, Projlocal, Dnum) VALUES ({}, {}, {})".format(ProjNum, i, j)
        cursor.execute(sql)
        connection.commit()
        ProjNum = ProjNum +1
    
cursor.close()




# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")