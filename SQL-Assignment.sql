CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);


CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);

INSERT INTO Members (id, name, age)
VALUES 
(1, 'John Davis', '87'),
(2, 'Marcus Johnson', '23'),
(3, 'Jane Doe', '40'),
(4, 'Carl Fellows', '32'),
(5, 'John Smith', '14'),
(6, 'Abner Steadman', '22'),
(7, 'Madison Gomez', '26');


INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
VALUES 
(1, 1, '2024-07-24', '3:52 PM', 'Weights'),
(2, 2, '2024-07-21', '2:12 PM', 'Pickle Ball'),
(3, 3, '2024-06-14', '9:01 AM', 'Track'),
(4, 4, '2024-05-12', '9:36 PM', 'Rock Climbing'),
(5, 5, '2024-07-21', '12:25 PM', 'Sauna'),
(6, 6, '2024-07-13', '3:45 PM', 'Weights'),
(7, 7, '2024-07-01', '6:41 AM', 'Cardio Station') ;

UPDATE WorkoutSessions 
SET session_time = '2:12 PM' 
WHERE session_id = 3 ; 

DELETE FROM WorkoutSessions 
WHERE member_id = 5;

DELETE FROM Members 
WHERE id = 5; 




SELECT * FROM  workoutsessions;

SELECT * FROM Members ;


 





