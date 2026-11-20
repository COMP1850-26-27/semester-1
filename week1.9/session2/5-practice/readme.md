
# SQL Task - create and manage a database

## Schema

We will create database for a small banking organisation with the following structure

- `Branch( branch_id(PK), street, city, postcode )`
- `Staff( staff_id(PK), name, role, branch(FK) )`

We will create the database one step at a time
- open the SQL interface for a new database with `sqlite3 branches.db`
- use `schema.sql` as a template for your code

Use documentation if you are not sure about the SQL commands. We will use:
- CREATE TABLE
- INSERT INTO
- UPDATE
- SELECT

## Task 1 - Branch relation

`Branch( branch_id(PK), street, city, postcode )`

### CREATE TABLE

Create the `Branch` relation using `CREATE TABLE Branch(...);` with appropriate attributes
- Think about the properties of the attributes
    - `branch_id` is integer, descriptive data is text
- Think about whether data can be NULL
    - eg. Branch address data should not be NULL

Test the `Branch` relation:
- visualise using `SELECT * FROM Branch;`
- it will show headers but no data.

### INSERT INTO

Add some data using `INSERT INTO Branch (...) VALUES (...);` with appropriate attributes and values
- eg. values `(1,'Shaw Lane','Leeds','LS6 5UL')`
- be careful with single quotes for 'text' (not " or `)

Test the `Branch` relation:
- visualise using `SELECT * FROM Branch;`
- you should now see the data in the table.

## Task 2 - Staff relation

`Staff( staff_id(PK), name, role, branch(FK) )`

### CREATE TABLE

Create the `Staff` relation
- Think about the properties of the attributes
    - `staff_id` is integer, descriptive data is text
- Think about whether data can be `NULL`
    - eg. Staff `role` and `branch` can be `NULL` until allocated
- `branch` is a foreign key, linked to `branch_id` in the `Branch` relation
    - add the annotation to the `Staff` relation (see the existing schema for an example)

Test the `Staff` relation.
- Test your design using `SELECT * FROM Staff;`

### INSERT INTO

Add some data using `INSERT INTO Staff (...) VALUES (...);`
- use appropriate attributes and choose some values for them, with `role` and `branch` both `NULL` initially.
- eg. values `(101,'Tom',NULL,NULL)`
- in reality we would first create a staff record then later allocate role and branch

Test the `Branch` relation:
- visualise using `SELECT * FROM Staff;`
- you should now see the data in the table.

## Task 3 - Allocate staff to a role and to a branch

### UPDATE

Once staff are created we can allocate them to a role and to a branch
- this sets the `NULL` values we created to real values
- `branch` is defined by the primary key of the `Branch` relation
- `role` is one of `Manager` or `Cashier`

Use `UPDATE` to set the staff role to `Manager`
- `UPDATE Staff SET role='Manager' WHERE staff_id=X;`
- `X` is the `staff_id` you have created

Use `UPDATE` to set the staff branch to the `branch_id` you created in the `Branch` table.

Use `SELECT * FROM Staff` to check that the relation is updated.

## Task 4 - Add more data

### INSERT and UPDATE

Add one more branch.

Add more staff so that each branch has at one Manager and at least one Cashier.

Test that the relations are updated and show all the data.

Test adding incorrect data
- add a branch with a repeated `branch_id`
- add a branch with a `NULL` city attribute
- how do the constraints set during the table creation in Task 1 affect this?

## Task 5 - Queries

### SELECT

Create some simple queries
- List all staff that are Managers
- List all staff at a single Branch

