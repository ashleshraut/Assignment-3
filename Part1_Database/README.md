# Part 1 — Relational Database Design, Querying, Indexing & Transactions

**Engine:** SQLite 3.45

## 1. Normalization Write-Up

### Unnormalized Representation (UNF)
An unnormalized representation of CampusConnect data would combine student, course, and enrollment information into a single flat structure with repeating fields:
`StudentCourse(StudentID, Name, Email, EnrolledCourseCodes, CourseTitles, Instructors, Grades)`

### Step-by-Step Normalization

1. **First Normal Form (1NF):**
   - *Requirement:* Eliminate repeating groups and ensure atomic values.
   - *Action:* Split repeating course lists into individual rows per enrollment.
   - *Result:* Primary Key becomes composite `(StudentID, CourseCode)`. Attributes: `StudentID, Name, Email, CourseCode, Title, InstructorName, Grade`.

2. **Second Normal Form (2NF):**
   - *Requirement:* Remove partial dependencies (non-key attributes dependent on only part of the composite primary key).
   - *Action:* `Title` and `InstructorName` depend solely on `CourseCode`, not `StudentID`. Separate into `Students`, `Courses`, and a junction table `Enrollments`.
   - *Dependencies Removed:* `CourseCode -> Title, InstructorName` (Partial Dependency).

3. **Third Normal Form (3NF):**
   - *Requirement:* Eliminate transitive dependencies (non-key attributes dependent on other non-key attributes).
   - *Action:* In `Courses`, `InstructorEmail` and `Department` depend on `InstructorName`. Extracted `Instructors` into its own relation referenced by `instructor_id`.
   - *Dependencies Removed:* `InstructorID -> Department` (Transitive Dependency).

---

## 2. Indexing Justification

- `idx_enrollments_student_id`: Speeds up joins and `WHERE student_id = ?` lookups in high-frequency student profile/dashboard queries.
- `idx_courses_credits_seats`: Composite index optimizing course search queries filtering by `credits` and `available_seats`.

### Intentional Unindexed Column Case
Columns like `enrollments.grade` or low-cardinality status flags are intentionally left unindexed. Indexing low-cardinality columns increases write overhead during updates/inserts without significantly reducing scan time during lookup queries.

---

## 3. Transactions and Isolation Analysis

### Race Condition Scenario
When two students simultaneously attempt to register for the last available seat in a course:
1. Both read `available_seats = 1`.
2. Both execute `UPDATE courses SET available_seats = available_seats - 1`.
3. Both insert an enrollment row, leading to `available_seats = -1` (Lost Update / Over-subscription).

### Isolation Level Prevention
- **Serializable Isolation** (or atomic checks with standard database transactions) prevents this by ensuring concurrent transactions execute sequentially relative to each other, forcing the second transaction to abort or read the updated state (`available_seats = 0`) and fail validation.
