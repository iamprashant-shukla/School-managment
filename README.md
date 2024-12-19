# School Management System

A Python-based **School Management System** designed to manage and organize data for schools. The system features role-based access where the **Principal** has full access to all data (teachers, students, and classes), while **Teachers** can only access data related to their assigned classes. Additionally, the project integrates with **Discord** to send updates via a webhook.

---

## Features

- **Role-Based Access**:
  - **Principal**:
    - Complete control over data (teachers, students, and classes).
  - **Teachers**:
    - Access restricted to their assigned classes and students.

- **Database-Driven**:
  - Uses **SQLite** for lightweight and efficient data management.
  - Data is stored in tables: `users`, `teachers`, `students`, `classes`, `class_teacher`, and `class_student`.

- **Discord Integration**:
  - Send important notifications (e.g., announcements, updates) to a Discord server via a webhook.

- **Simple Command-Line Interface**:
  - Intuitive menu-based navigation for data access and operations.

- **Easy Setup**:
  - The project includes all necessary scripts to initialize the database and get started quickly.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Discord Integration](#discord-integration)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Project Structure

The project is organized as follows:
school-management-system/

    ├── database/
    │   ├── initialize_db.py  # Script to create and populate the database
    │   ├── school.db         # SQLite database file
    ├── utils/
    │   ├── queries.py        # Functions to interact with the database
    │   ├── discord_bot.py    # Logic for sending updates to Discord
    ├── main.py                # Main application entry point
    ├── requirements.txt       # Python dependencies
    ├── README.md              # Project documentation (this file)
    └── .gitignore             # Ignored files (e.g., *.pyc, .env)




---
## Usage

- **View Teachers**: Displays teacher details.
- **View Students**: Displays student details.
- **Exit**: Exit the app.

---

## Database Schema

- **users**: Stores login credentials (role: `principal` or `teacher`).
- **teachers**: Information about teachers (name, subject, etc.).
- **students**: Information about students (class_id, parent contact, etc.).
- **classes**: List of classes.
- **class_teacher**: Mapping between classes and teachers.
- **class_student**: Mapping between students and classes.


## Installation

### Prerequisites
- Python 3.7 or higher installed on your system.

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/school-management-system.git
   cd school-management-system
   

## License

[MIT License.](https://choosealicense.com/licenses/mit/)  See the LICENSE file for details.




