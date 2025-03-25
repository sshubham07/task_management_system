# Task Management System

A Django-based Task Management API that allows task creation,user creation,  user assignment, and task tracking.

## Setup Project

1. **Clone the Repository**
```bash
git clone https://github.com/sshubham07/task_management_system.git
```

2. **Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate 
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Development Server**
```bash
cd task_management_system
python manage.py runserver
```

## API Endpoints

1. **User Registration**
   - URL: `/api/register/`
   - Method: `POST`
   - Payload:
     ```json
     {
       "username": "your_username",
       "password": "your_password",
       "email": "your_email@example.com"
     }
     ```

2. **Get Tasks Assigned to a User**
   - URL: `/api/user-tasks/<user_id>/`
   - Method: `GET`

3. **Assign Task to Users**
   - URL: `/api/assign-task/`
   - Method: `POST`
   - Payload:
     ```json
     {
       "task_id": 1,
       "user_id": 1
     }
     ```

## Testing the API

You can test the API using tools like:

- **Django Browsable API**: Navigate to `http://localhost:8000/api/` in your browser.
- **cURL**: Send requests from the command line.
- **Postman/Insomnia**: For GUI-based API testing.
### ➤ Sample Admin User
For quick access to the **Django Admin Panel** (`http://localhost:8000/admin/`), you can use the following sample credentials:

```bash
Username: rahul
Password: 123


