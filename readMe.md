Course Management System

Architecture

The Course Management System is built using the Django MVC (Model-View-Controller) architecture, which consists of:

Models: Define the database schema for courses, students, and enrollments.

Views: Handle business logic for course creation, student registration, and enrollment.

Templates: Provide HTML pages for user interaction.

Admin Interface: Built-in Django admin panel for managing courses and students.

Features

Admin Functionalities:

Create courses with categories (Video, Document, MCQ Quiz).

Register students with name and email (credentials emailed to students).

Enroll students into courses.

View all enrolled students in the admin dashboard.

Student Functionalities:

View available courses.

Installation

1. Clone the Repository

git clone https://github.com/your-repo/course-management.git
cd course-management

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies

pip install django

4. Configure Database and Migrations

python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Admin)

python manage.py createsuperuser

Follow the prompts to set up an admin account.

6. Run the Development Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

Usage

Access the Django Admin Panel at http://127.0.0.1:8000/admin/.

Create courses, students, and enrollments using the admin dashboard.

Students will receive emails upon registration with login credentials.

View enrolled students from the admin dashboard.

