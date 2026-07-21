PRAGMA foreign_keys = ON;

-- Insert Instructors (10 rows)
INSERT INTO instructors (first_name, last_name, email, department) VALUES
('Alan', 'Turing', 'alan.turing@campusconnect.edu', 'Computer Science'),
('Ada', 'Lovelace', 'ada.lovelace@campusconnect.edu', 'Computer Science'),
('Grace', 'Hopper', 'grace.hopper@campusconnect.edu', 'Software Engineering'),
('Edsger', 'Dijkstra', 'edsger.dijkstra@campusconnect.edu', 'Computer Science'),
('Donald', 'Knuth', 'donald.knuth@campusconnect.edu', 'Algorithms'),
('Claude', 'Shannon', 'claude.shannon@campusconnect.edu', 'Information Theory'),
('Barbara', 'Liskov', 'barbara.liskov@campusconnect.edu', 'Software Systems'),
('John', 'von Neumann', 'john.vonneumann@campusconnect.edu', 'Mathematics'),
('Tim', 'Berners-Lee', 'tim.bl@campusconnect.edu', 'Web Technologies'),
('Linus', 'Torvalds', 'linus.torvalds@campusconnect.edu', 'Operating Systems');

-- Insert Students (10 rows)
INSERT INTO students (first_name, last_name, email, enrollment_year) VALUES
('Alice', 'Smith', 'alice.smith@student.edu', 2023),
('Bob', 'Jones', 'bob.jones@student.edu', 2023),
('Charlie', 'Brown', 'charlie.brown@student.edu', 2024),
('Diana', 'Prince', 'diana.prince@student.edu', 2022),
('Evan', 'Wright', 'evan.wright@student.edu', 2024),
('Fiona', 'Gallagher', 'fiona.gallagher@student.edu', 2023),
('George', 'Clark', 'george.clark@student.edu', 2025),
('Hannah', 'Abbott', 'hannah.abbott@student.edu', 2022),
('Ian', 'Malcolm', 'ian.malcolm@student.edu', 2024),
('Julia', 'Roberts', 'julia.roberts@student.edu', 2023);

-- Insert Courses (10 rows)
INSERT INTO courses (course_code, title, credits, available_seats, instructor_id) VALUES
('CS101', 'Intro to Computer Science', 3, 29, 1),
('CS102', 'Data Structures & Algorithms', 4, 25, 2),
('CS201', 'Database Systems', 3, 19, 3),
('CS202', 'Operating Systems', 4, 15, 10),
('CS301', 'Computer Networks', 3, 20, 6),
('CS302', 'Software Architecture', 3, 12, 7),
('CS401', 'Cryptography & Security', 4, 10, 4),
('CS402', 'Distributed Systems', 4, 8, 8),
('WEB101', 'Web Development Basics', 3, 30, 9),
('MATH201', 'Discrete Mathematics', 3, 22, 5);

-- Insert Enrollments (10 rows)
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2024-01-15', 'A'),
(1, 3, '2024-01-16', 'B'),
(2, 1, '2024-01-15', 'A'),
(2, 2, '2024-01-17', 'C'),
(3, 3, '2024-01-18', 'A'),
(4, 4, '2024-01-19', 'B'),
(5, 5, '2024-01-20', NULL),
(6, 6, '2024-01-21', 'A'),
(7, 7, '2024-01-22', NULL),
(8, 8, '2024-01-23', 'F');

-- Foreign Key Violation Demonstration (Commented out so script runs cleanly):
-- INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (999, 1, '2024-01-24', 'A');
-- Error: FOREIGN KEY constraint failed because student_id 999 does not exist in students.
