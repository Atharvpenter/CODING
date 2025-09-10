use atharv;

CREATE TABLE trainers (
    trainer_id INT PRIMARY KEY AUTO_INCREMENT,
    trainer_name VARCHAR(20) NOT NULL,
    trainer_lname VARCHAR(20),
    email VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(20),
    expertise VARCHAR(200),
    date_of_joining DATE NOT NULL,
    previous_experience INT DEFAULT 0, -- in years
    assigned_course_id INT,
    workmode CHAR(10) DEFAULT 'WFO'
);


INSERT INTO trainers 
(trainer_name, trainer_lname, email, phone, expertise, date_of_joining, previous_experience, assigned_course_id, workmode)
VALUES
('Rahul', 'Dravid', 'rahul.dravid@bcci.in', '9876543210', 'Python, Data Structures, System Design', '2021-11-01', 15, 1, 'WFO'),

('Vikram', 'Rathour', 'vikram.rathour@bcci.in', '9876543211', 'SQL, Backend Development, Data Analytics', '2019-09-01', 12, 2, 'WFH'),

('Paras', 'Mhambrey', 'paras.mhambrey@bcci.in', '9876543212', 'Big Data, Distributed Systems, Cloud Computing', '2021-11-01', 10, 3, 'Remote'),

('T', 'Dilip', 'tdilip@bcci.in', '9876543213', 'Frontend, Fullstack, UI/UX', '2021-09-01', 9, 4, 'WFO'),

('Paddy', 'Upton', 'paddy.upton@bcci.in', '9876543214', 'Data Science, AI, Machine Learning, SQL', '2022-07-01', 20, 5, 'Remote');



-- New Hybrid Trainers
INSERT INTO trainer_latest 
(trainer_name, trainer_lname, email, phone, expertise, date_of_joining, previous_experience, assigned_course_id, workmode)
VALUES

('Anil', 'Kumble', 'anil.kumble@bcci.in', '9876543215', 'DevOps, Docker, Kubernetes, Backend', '2020-01-15', 18, 6, 'Hybrid'),

('Ramesh', 'Powar', 'ramesh.powar@bcci.in', '9876543216', 'Data Engineering, Big Data, ETL, SQL', '2018-03-10', 14, 7, 'Hybrid');
select * from trainers;
