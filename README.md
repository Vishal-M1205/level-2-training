# LEVEL 2 — Python & Backend Development Portfolio

This repository contains completed Python assignments, layered OOP applications, FastAPI + PostgreSQL backend projects, and presentation materials completed during Level 2 training.

---

## Completed Assignments & Projects

### 1. Python Assignment 1 — Core Python & Console Applications
**Folder:** `Python/ASSIGNMENT 1`

A collection of 14 standalone Python scripts progressing from basic conditionals and loops to interactive menu-driven console applications:
- **Control Flow & Logic:** `electricity_bill.py`, `login_system.py`, `number_analyzer.py`, `menu_based_number_analyzer.py`
- **Built-in Data Structures:** `list_functionalities.py`, `dict_functionalities.py`, `set_functionalities.py`
- **Calculators & Analyzers:** `shopping_cart_calculator.py`, `employee_salary_analyzer.py`, `student_result_analyzer.py`
- **Console Mini-Applications:** `atm_transaction_simulation.py`, `employee_management_console.py`, `student_management_console.py`, `11_mini_banking_app.py`

**Concepts Covered:**
- Variables, expressions, and conditional branching (`if`/`elif`/`else`)
- Loops (`for`, `while`), menu-driven control flow, and input handling
- Core data structures: `list`, `dict`, and `set` operations
- Reusable functions, parameter passing, and standard library usage (`math`)
- In-memory CRUD operations and basic transaction/account simulations

---

### 2. Python Assignment 2 — Modular Functions & Data Processing
**Folder:** `Python/ASSIGNMENT 2`

Builds on Assignment 1 by decomposing larger console programs into focused helper functions and performing richer in-memory data analysis (`employee_management.py`, `rewrite_atm_program.py`, `prac.py`).

**Concepts Covered:**
- Function decomposition (separating input collection, validation, display, and business logic)
- Aggregation and reporting (total counts, department-wise counts, department-wise highest salary)
- Filtering, searching, and sorting collections (sorting employees by salary)
- Code refactoring from monolithic scripts into cleaner function-based workflows

---

### 3. Membership Management System (Modular CLI)
**Folder:** `Python/membership_system`

A multi-module console application (`main.py` + `modules/`) for managing members and membership plans with persistent JSON storage (`member_data/members.json`, `member_data/memberships.json`).

**Concepts Covered:**
- Package and module separation (`config.py`, `json_services.py`, `member_services.py`, `membership_services.py`, `validators.py`)
- Structural pattern matching (`match`/`case`) for CLI menu dispatch
- File I/O and JSON serialization/deserialization (`json.load`, `json.dump`)
- Path handling with `pathlib.Path` and environment configuration via `.env`
- Exception handling for file and data errors (`FileNotFoundError`, `json.JSONDecodeError`)
- Input validation before persisting records

---

### 4. Membership Management System (Layered OOP Architecture)
**Folder:** `Python/membership_system_oops`

An object-oriented, production-structured evolution of the Membership System organized into `core/`, `models/`, `repositories/`, `services/`, `validators/`, `exceptions/`, `util/`, and `test/`, supporting both CSV and JSON persistence (`data/`).

**Concepts Covered:**
- **Object-Oriented Design & Abstraction:** Abstract base class `DataRepository` (`abc.ABC`, `@abstractmethod`) with interchangeable `CSVRepository` and `JSONRepository` implementations
- **Layered Architecture & Dependency Injection:** Clear separation between Models, Repositories, Services, Validators, and CLI Utilities
- **Data Modeling & Validation:** `pydantic` (`BaseModel`, `Field` constraints) and dedicated validator classes
- **Custom Exception Handling:** Domain-specific exceptions (`exceptions/member_exception.py`, `exceptions/membership_exception.py`)
- **Asynchronous Execution:** `asyncio` event loop and async UI helpers
- **Logging & Reporting:** Configured file/console logging (`app.log`, `util/log.py`) and text report generation (`member_details.txt`, `util/member_report.py`)
- **Unit Testing:** Automated tests and fixtures using `pytest` (`conftest.py`, `test/test_member_service.py`, `test/test_validation.py`)

---

### 5. Student Management API — FastAPI & PostgreSQL Projects
**Base Folder:** `Python/student_fastAPI_project`

A progression from raw SQL schema design to a full-featured FastAPI + PostgreSQL backend, implemented first with `psycopg` and then refactored to SQLAlchemy ORM with Alembic migrations.

#### 5a. SQL Schema & Seed Data
**Folder:** `Python/student_fastAPI_project/sql_query` (`student.sql`)

**Concepts Covered:**
- PostgreSQL DDL (`CREATE TABLE`, `SERIAL PRIMARY KEY`, `NUMERIC(5,2)`)
- Relational modeling with foreign key constraints across `students`, `subjects`, `marks`, and `grades`
- Seeding relational test data with `INSERT INTO`

#### 5b. Student Management API (Psycopg)
**Folder:** `Python/student_fastAPI_project/Student Management API Psycopg`

An asynchronous FastAPI REST API connected directly to PostgreSQL using `psycopg` and `psycopg-pool`.

**Concepts Covered:**
- FastAPI application lifecycle (`@asynccontextmanager` lifespan) managing an async `psycopg_pool` on `app.state`
- Modular API architecture (`routes/`, `services/`, `repositories/`, `schemas/`, `core/`, `utils/`)
- Dependency Injection with `Depends` and `typing.Annotated`
- Pydantic request/response schemas (Create, Update, Patch, List/Response models)
- Query pagination & filtering (`Query`), HTTP headers (`Header`), cookies (`Response.set_cookie`), and multipart file uploads (`UploadFile`)
- Structured application logging (`app.log`) and `.env` settings via `pydantic-settings`

#### 5c. Student Management API (SQLAlchemy ORM)
**Folder:** `Python/student_fastAPI_project/Student Management API SQLAlchemy(orm)`

A refactored version of the Student Management API using SQLAlchemy 2.x ORM, repository interfaces, Alembic database migrations, and automated tests.

**Concepts Covered:**
- **SQLAlchemy 2.x ORM:** Declarative models (`Base`, `Mapped`, `mapped_column`, `relationship`) for `Student`, `Subject`, `ExamMark`, `IdCard`, and class entities
- **Interface-Driven Design:** Abstract repository/service interfaces (`app/interfaces/`)
- **Database Migrations:** Schema versioning and constraint updates with Alembic (`alembic.ini`, `migrations/versions/`)
- **Global Exception Handling:** FastAPI `@app.exception_handler` for `IntegrityError` (`409 Conflict`) and unhandled exceptions (`500 Internal Server Error`)
- **Automated Testing:** Route and service tests with `pytest` (`tests/conftest.py`, `tests/test_result_service.py`, `tests/test_student_routes.py`, `tests/test_subject_routes.py`)

---

### 6. Presentation — Abstraction, Interface, and Protocol in Python
**Folder:** `Presentation/Abstraction, Interface, Protocol`

Includes the slide deck (`Abstraction-Interface-and-Protocol-in-Python.pptx`) and runnable code examples demonstrating Python's approaches to abstraction and polymorphism.

**Concepts Covered:**
- Good vs. bad abstraction design (`bad_abstraction.py`, `good_abstraction.py`)
- Abstract Base Classes (`abc_abstraction.py`) and ABC-based interfaces (`interface_abc.py`)
- Dynamic polymorphism via duck typing (`ducktyping.py`)
- Structural subtyping and static type checking with `typing.Protocol` (`protocol_statictype.py`)
