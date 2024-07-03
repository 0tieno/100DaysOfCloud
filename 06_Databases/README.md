# day 01

* Used the CREATE statement to create databases and tables. e.g `CREATE DATABASE database_name;`, `CREATE TABLE table_name (column1 datatype, column2 datatype, ...);`
* Used the SHOW statement to view available databases and tables. e.g `SHOW DATABASES;`, `SHOW TABLES;`
* Used the ALTER statement to alter the structure of a table. e.g `ALTER TABLE table_name ADD column_name datatype;`
* Used the DROP statement to delete databases and tables. e.g `DROP DATABASE database_name;`, `DROP TABLE table_name;`

**Database** is a collection of tables. It is a container for tables. It is used to store data in an organized manner.

**Table** is a collection of rows and columns. It is used to store data in a structured format.

**Column** is a vertical entity in a table that contains all information associated with a specific field in a table.

**Row** is a horizontal entity in a table that contains all information about a specific item in a table.

**Primary Key** is a column that uniquely identifies each row in a table. It must contain a unique value for each row of data.

**Foreign Key** is a column that creates a relationship between two tables. It is a field in a table that is the primary key in another table.

**Data Types** are used to define the type of data that can be stored in a column. Some common data types are INT, VARCHAR, DATE, and TEXT.

**CREATE DATABASE** statement is used to create a new database in MySQL.

**CREATE TABLE** statement is used to create a new table in a database.

**SHOW DATABASES** statement is used to display a list of all databases in MySQL.

**SHOW TABLES** statement is used to display a list of all tables in a database.

**ALTER TABLE** statement is used to add, delete, or modify columns in a table.

**DROP DATABASE** statement is used to delete a database in MySQL.

**DROP TABLE** statement is used to delete a table in a database.

**INSERT INTO** statement is used to insert new records into a table. e.g `INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);`

**SELECT** statement is used to retrieve data from a table. e.g `SELECT column1, column2, ... FROM table_name;`

**UPDATE** statement is used to modify existing records in a table. e.g `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;`

**DELETE** statement is used to delete existing records from a table. e.g `DELETE FROM table_name WHERE condition;`

**ORDER BY** statement is used to sort the result set in ascending or descending order. e.g `SELECT column1, column2, ... FROM table_name ORDER BY column1 ASC/DESC;`

**GROUP BY** statement is used to group rows that have the same values into summary rows. e.g `SELECT column1, COUNT(column2) FROM table_name GROUP BY column1;`

**JOIN** statement is used to combine rows from two or more tables based on a related column between them. e.g `SELECT column1, column2, ... FROM table1 JOIN table2 ON table1.column_name = table2.column_name;`
