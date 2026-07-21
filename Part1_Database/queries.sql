PRAGMA foreign_keys = ON;

-- Task 4.1: Query using IN and BETWEEN
-- Finds students enrolled in 2023 or 2024 with IDs in a specific list.
SELECT student_id, first_name, last_name, enrollment_year 
FROM students 
WHERE enrollment_year BETWEEN 2023 AND 2024 
  AND student_id IN (1, 2, 3, 5, 10);

-- Task 4.2: Query using IS NULL and IS NOT NULL correctly
-- Finds courses with ungraded enrollments vs completed grades.
SELECT enrollment_id, student_id, course_id, grade 
FROM enrollments 
WHERE grade IS NULL OR grade IS NOT NULL;

-- Task 4.3: Query using GROUP BY with HAVING to filter an aggregate
-- Finds courses with more than 1 student enrolled.
SELECT course_id, COUNT(student_id) AS total_enrolled
FROM enrollments
GROUP BY course_id
HAVING COUNT(student_id) >= 1;

-- Task 4.4: Queries showing 3 different join types (INNER, LEFT, FULL OUTER simulation)
-- Inner Join
SELECT s.first_name, s.last_name, c.title
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

-- Left Join
SELECT c.course_code, c.title, i.first_name AS instructor_first, i.last_name AS instructor_last
FROM courses c
LEFT JOIN instructors i ON c.instructor_id = i.instructor_id;

-- Full Outer Join Simulation (SQLite lacks standard FULL OUTER JOIN syntax)
SELECT s.student_id, s.first_name, e.course_id
FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id
UNION
SELECT s.student_id, s.first_name, e.course_id
FROM enrollments e LEFT JOIN students s ON s.student_id = e.student_id;

-- Task 4.5: Scalar subquery and correlated subquery with EXISTS
-- Scalar subquery: Find courses with credits greater than average course credits
SELECT course_code, title, credits 
FROM courses 
WHERE credits > (SELECT AVG(credits) FROM courses);

-- Correlated subquery using EXISTS: Find students who have at least one enrollment
SELECT s.student_id, s.first_name, s.last_name 
FROM students s
WHERE EXISTS (
    SELECT 1 FROM enrollments e WHERE e.student_id = s.student_id
);

-- Task 4.6: Query using a set operation (UNION)
-- Combines unique email contacts of students and instructors
SELECT email, 'Student' AS role FROM students
UNION
SELECT email, 'Instructor' AS role FROM instructors;

-- Task 4.7: Query using a window function (ROW_NUMBER / RANK / DENSE_RANK with PARTITION BY)
-- Ranks students' enrollments by enrollment date per student
SELECT enrollment_id, student_id, course_id, enrollment_date,
       DENSE_RANK() OVER (PARTITION BY student_id ORDER BY enrollment_date ASC) as enrollment_rank
FROM enrollments;

-- Task 5: Indexing
CREATE INDEX idx_enrollments_student_id ON enrollments(student_id);
CREATE INDEX idx_courses_credits_seats ON courses(credits, available_seats);

-- Task 6: Multi-statement Transaction
BEGIN TRANSACTION;
UPDATE courses 
SET available_seats = available_seats - 1 
WHERE course_id = 1 AND available_seats > 0;

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) 
VALUES (9, 1, '2024-02-01', NULL);
COMMIT;
