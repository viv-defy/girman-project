# girman-project

This is an Role-Based Access Control (RBAC) System to manage user roles and permissions dynamically.

## Deployment details

Deployed on render - https://girman-project.onrender.com

Language - Python 3.12

Databases - Postgres

Postman Collection - [JSON file](/postman-collection.json) within the repo

## Setup

1. Download/clone the [repo](git@github.com:viv-defy/girman-project.git) onto local

   ```
   git clone git@github.com:viv-defy/girman-project.git
   cd girman-project
   ```

2. Ensure you have python3.12. If not download from [here](https://www.python.org/downloads/release/python-3127/)

3. Set up your local env and run

   On linux and mac

   ```
   python3.12 -m venv env
   source env/bin/activate
   ```

   On Windows

   ```
   python3.12 -m venv env
   .\env\bin\activate
   ```

4. Run the build script (for Unix-based systems)

   ```
   sh build.sh
   ```

   This will install the requirements and apply initial migrations.

   In case you are on Windows, run the following in your powershell

   ```
   pip install -r requirements.txt

   python manage.py migrate
   ```

5. Run Django server
   ```
   python manage.py runserver
   ```

This should start the app on your [local](http://localhost:8000)

## Improvements

1. The app could be named rbac instead of users. This would ensure cleaner and more meaningful urls for the apis
