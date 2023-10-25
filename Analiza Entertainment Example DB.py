import pyodbc
import pandas as pd

print(pyodbc.drivers())

conn = pyodbc.connect(
    Trusted_Connection = "Yes",
    Driver = 'ODBC Driver 17 for SQL Server',
    Server = 'Kuba',
    Database = 'EntertainmentAgencyExample',
    autocommit = True
)

#Nazwy Tabel postaci tabeli

print("Nazwy tabel w bazie danych")
query = "SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'"
my_cursor = conn.cursor()

my_cursor.execute(query)

table_names = [row.table_name for row in my_cursor.fetchall()]

Data_Frame_Nazwy_Tabel = pd.DataFrame(table_names, columns=["Nazwa Tabeli"])

print(Data_Frame_Nazwy_Tabel)

my_cursor.fetchall()

# Tabela Agents
query1 = "SELECT * FROM Agents"

my_cursor1 = conn.cursor()

my_cursor1.execute(query1)

for x in my_cursor1:
    print(x)

