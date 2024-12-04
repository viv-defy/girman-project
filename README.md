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

## Testing the App/End Points

1. As the app starts, you can login to admin panel using default superuser details (sent in mail)
2. On the admin panel, you have by default

   1. Users - admin
   2. Roles - staff, supervisor, admin
   3. Permissions - level1, level2, level3, super

   Further details about the same can be viewed in admin details

3. Add Token

   1. You can access the tokens table to add tokens to admin(user)

4. Setup Postman

   1. Import postman-collection.json into your postman app
   2. Use the token created in step 3.1
   3. Setup token in you postman variables

5. Run the management endpoints on Postman to create users, assign roles and permissions

## Improvements

1. The app could be named rbac instead of users. This would ensure cleaner and more meaningful urls for the apis
