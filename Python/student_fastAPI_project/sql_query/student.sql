CREATE TABLE students (
id SERIAL PRIMARY KEY,
name VARCHAR NOT NULL,
age INTEGER NOT NULL,
gender CHAR NOT NULL
);

CREATE TABLE subjects (
id SERIAL PRIMARY KEY,
name VARCHAR NOT NULL 
);

CREATE TABLE marks (
id SERIAL PRIMARY KEY,
subject_id INTEGER NOT NULL,
student_id INTEGER NOT NULL,
mark NUMERIC(5,2) NOT NULL,

CONSTRAINT fk_subject_id 
FOREIGN KEY (subject_id) REFERENCES 
subjects(id),

CONSTRAINT fk_student_id
FOREIGN KEY (student_id) REFERENCES 
students(id)
);

CREATE TABLE grades (
id SERIAL PRIMARY KEY,
student_id INTEGER NOT NULL,
total_marks NUMERIC(5,2) NOT NULL,
grade CHAR NOT NULL,

CONSTRAINT fk_student_id
FOREIGN KEY (student_id) REFERENCES 
students(id)
);

INSERT INTO students (name, age, gender) VALUES
('Arun Kumar', 20, 'M'),
('Priya Sharma', 21, 'F'),
('Rahul Raj', 19, 'M'),
('Divya Krishnan', 20, 'F'),
('Karthik S', 22, 'M'),
('Sneha Devi', 19, 'F'),
('Vignesh Kumar', 21, 'M'),
('Ananya R', 20, 'F'),
('Sanjay Kumar', 22, 'M'),
('Keerthana M', 19, 'F');

INSERT INTO subjects (name) VALUES
('Mathematics'),
('Physics'),
('Chemistry'),
('Computer Science'),
('English');

INSERT INTO marks (student_id, subject_id, mark) VALUES
-- Student 1
(1, 1, 85.00),
(1, 2, 78.00),
(1, 3, 92.00),
(1, 4, 88.00),
(1, 5, 81.00),

-- Student 2
(2, 1, 72.00),
(2, 2, 80.00),
(2, 3, 75.00),
(2, 4, 91.00),
(2, 5, 84.00),

-- Student 3
(3, 1, 95.00),
(3, 2, 89.00),
(3, 3, 93.00),
(3, 4, 97.00),
(3, 5, 90.00),

-- Student 4
(4, 1, 68.00),
(4, 2, 74.00),
(4, 3, 70.00),
(4, 4, 82.00),
(4, 5, 76.00),

-- Student 5
(5, 1, 88.00),
(5, 2, 85.00),
(5, 3, 79.00),
(5, 4, 94.00),
(5, 5, 87.00),

-- Student 6
(6, 1, 76.00),
(6, 2, 69.00),
(6, 3, 82.00),
(6, 4, 78.00),
(6, 5, 73.00),

-- Student 7
(7, 1, 91.00),
(7, 2, 86.00),
(7, 3, 89.00),
(7, 4, 92.00),
(7, 5, 85.00),

-- Student 8
(8, 1, 64.00),
(8, 2, 71.00),
(8, 3, 67.00),
(8, 4, 79.00),
(8, 5, 74.00),

-- Student 9
(9, 1, 83.00),
(9, 2, 77.00),
(9, 3, 85.00),
(9, 4, 89.00),
(9, 5, 80.00),

-- Student 10
(10, 1, 70.00),
(10, 2, 65.00),
(10, 3, 73.00),
(10, 4, 81.00),
(10, 5, 69.00);

INSERT INTO grades (student_id,total_marks,grade)
SELECT student_id, 
SUM(mark) as total_marks,
CASE 
 WHEN SUM(mark) >= 450 THEN 'A'
 WHEN SUM(mark) >= 350 THEN 'B'
 WHEN SUM(mark) >= 300 THEN 'C'
 ELSE 'F'
 END as grade
FROM marks
GROUP BY student_id;

SELECT * FROM students;

ALTER TABLE marks DROP CONSTRAINT fk_subject_id;
ALTER TABLE grades DROP CONSTRAINT fk_student_id;

ALTER TABLE marks 
  ADD CONSTRAINT fk_subject_id 
  FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE;

ALTER TABLE grades 
  ADD CONSTRAINT fk_student_id FOREIGN KEY (student_id) 
  REFERENCES students(id);