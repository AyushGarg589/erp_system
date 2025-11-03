CREATE DATABASE Students ; 

USE Students ;


CREATE TABLE student_data(
    roll_no BIGINT PRIMARY KEY ,
    name VARCHAR(50) NOT NULL , 
    branch VARCHAR(100) , 
    sec VARCHAR(5)
);



SELECT * FROM student_data ;






   INSERT INTO student_data (student_name , student_number , student_branch , student_section )
                VALUES (%s , %s , %s , %s) , (student_name ,student_number , student_branch , student_section , ) 
    
    cur.execute(query)