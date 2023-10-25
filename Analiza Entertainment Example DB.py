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
query = "SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'"
my_cursor = conn.cursor()

my_cursor.execute(query)

table_names = [row.table_name for row in my_cursor.fetchall()]

conn.close()

Data_Frame_Nazwy_Tabel = pd.DataFrame(table_names, columns=["Nazwa Tabeli"])

print(Data_Frame_Nazwy_Tabel)
