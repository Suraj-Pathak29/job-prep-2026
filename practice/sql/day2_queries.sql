-- Create a Student Table
Create table students(
    id integer,
    name text,
    age integer,
    marks integer
);

-- Insert data
Insert into students values(1,'Rahul',20,85);
Insert into students values(2,'Anita',22,90);
Insert into students values(3,'Suraj',21,78);
Insert into students values(4,'Priya',19,88);
Insert into students values(5,'Amit',23,65);



-- Select all records
SELECT * 
from students;


-- Select specific columns
SELECT name,marks
from students;


-- Filter using WHERE
select *
from students
where marks >= 85;


-- Use AND / OR
select * 
from students 
where age < 21 and marks >= 85;

SELECT * 
from students 
where marks >= 85 or age > 21;


-- Sort results
select name , age
from students
order by age desc;


-- Limit output
select *
from students 
order by marks desc limit 3;