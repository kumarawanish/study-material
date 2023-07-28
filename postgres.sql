1.We want to change the data type of the year column of the cars table from INT to VARCAHR(4).

ALTER TABLE cars
ALTER COLUMN year TYPE VARCHAR(4);

2.Change the color column from VARCHAR(255) to VARCHAR(30):

    ALTER TABLE cars
    ALTER COLUMN color TYPE VARCHAR(30);

3.DROP COLUMN
We want to remove the column named color from the cars table.

To remove a column, use the DROP COLUMN statement:
    ALTER TABLE cars
    DROP COLUMN color;

4.The DELETE Statement
    The DELETE statement is used to delete existing records in a table.

    DELETE FROM cars
    WHERE brand = 'Volvo';

5.Delete all records in the cars table:

    TRUNCATE TABLE cars;

6.Delete the cars table:
    DROP TABLE cars;


7.Return all customers with a name that starts with the letter 'A':
    SELECT * FROM customers
    WHERE customer_name LIKE 'A%';


Note: The LIKE operator is case sensitive, if you want to do a case insensitive search, use the ILIKE operator instead.

8.Return all customers with a name that contains the letter 'A' or 'a':

    SELECT * FROM customers
    WHERE customer_name ILIKE '%A%';

9.Return all customers with a name that ends with the phrase 'en':
    SELECT * FROM customers
    WHERE customer_name LIKE '%en';
