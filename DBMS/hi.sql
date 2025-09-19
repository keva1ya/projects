-- Simple SQL code to create a table and insert a row

CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(50)
);

INSERT INTO Students (ID, Name) VALUES (1, 'Alice');

SELECT * FROM Students;