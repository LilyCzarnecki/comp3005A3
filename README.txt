In PostGreSQL have a database
- note down what the database name is, username and password

in the code replace dbName with the database name, username with the username and passWord with the password for the database. host can be likely be replaced with localhost, and port with 5432
(The line in question:)
--> connection = psycopg2.connect(dbname="dbName", user="username", password="passWord", host="host", port="port")

then simply run and type in either 'get', 'add', 'update', or 'remove', based on what query you want to run (or stop the program with 'end')

Video link:
https://youtu.be/MMIBkasuYks