import mysql.connector
from tabulate import tabulate

testdb = mysql.connector.connect (
host = 'localhost',
user = 'root',
database = 'herosql',
password = 'gintoki00'
)

mytest = testdb.cursor()
mytest.execute('show tables')
result = mytest.fetchall()
head = [i[0] for i in mytest.description]
finalresults = tabulate(result,headers=head,tablefmt='psql')
print(finalresults)
