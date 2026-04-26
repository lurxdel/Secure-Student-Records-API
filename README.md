# Secure Student Records API

This project is a **Secure Web-based API** built using the Django REST Framework. It is designed to handle **Role-Based Access Control (RBAC)** alongside standard **JWT Authentication**, ensuring strict authorization hierarchies on academic datasets.

### Features
- **JWT Authentication:** Implements `djangorestframework-simplejwt` to safely issue and verify access tokens.
- **Role-Based Access Control:** Preconfigures Django's native Group models to distinctively identify standard `Admin`, `Faculty`, and `Student` accounts.
- **Custom App Authorizations:** Deploys a custom `IsAdminOrFaculty` permission class mapped natively within the API view securing endpoints so only elevated users can edit or remove models.
- **Dynamic Data Visualization:** Dynamically limits students globally to only retrieve entries explicitly owned by their accounts.

## Guide To Run
To run the system locally, do the following.
> - **Clone this repository** or download it as a **ZIP file.**
> - When cloning the repository, follow these steps.

### 1. Install Python
- You can get it from here. [Python.org](https://www.python.org/)

### 2. Setting up the Backend
Navigate to the directory and configure the environment:

```bash
# Navigate to the correct directory containing manage.py
cd Secure-Student-Records-API

# (Optional but recommended) Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# Install the required frameworks for this project
pip install django djangorestframework djangorestframework-simplejwt

# Run the database migrations to set up the SQLite tables
python manage.py migrate

# Initialize setup groups and dummy testing accounts (Optional testing script)
python create_test_users.py

# Start the development server
python manage.py runserver
```

The server should now be running.

### 3. Available Endpoints
You can utilize endpoints via API consumers like **Postman** referencing localhost (`http://127.0.0.1:8000/`) :

- **Token Generator View:** `POST /api/token/` - Insert a JSON body of your username and password to retrieve token authentication.
- **Student Data View:** `GET, POST, PATCH /api/student-records/` - Primary endpoint executing full CRUD actions backed by role-level restrictions.

### Acknowledgment  
We are grateful to our instructors for their guidance and support throughout the development of this project. 

This work reflects my learning journey as a programmer.

## Disclaimer 
<div align="center"> 
  I do not own the names, information or references included in this project they are used purely as placeholders. <br> 
  All trademarks, service marks, trade names, and other intellectual property rights belong to their respective owners.  <br><br>

  Made with 💗 by <a href="https://github.com/lurxdel"><strong>Lurxdel</strong></a>
</div>
