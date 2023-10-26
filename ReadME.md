# To Restore Bank Data

1. Create a postgres database.
2. Restore the Banks and their Branch details from [Indian banks Repository](https://github.com/snarayanank2/indian_banks).


# Project Breakdown steps

1. Create virtualenv and activate it.
    ```
    virtualenv .venv

    source .venv/bin/activate
    ```


2. Install django and djangorestframework to create the Rest API.
    ```
    pip install django djangorestframework
    ```

3. Create new django project.
    ```
    django-admin startproject Banks
    ```

4. create new django app in project root directory which will store apis for banks.
    ```
    djangop-admin startapp apis
    ```

5. Create models for Tables present in the database in apis/models.py
    ```
    python manage.py inspectdb > apis/models.py
    ```


6. Add one more model for bank_branches view in database and if any change in models if required.

7. Register models in admin.py and run migrations.
    ```
    python manage.py makemigrations

    python manage.py migrate
    ```

8. Add serializers in apis/serializers.py for Bank model(based on Bank table of database) and BankBranch models(based in view of database).

9. Write views for BankList, BankDetail, BankBranchList and BranchDetail in apis/views.py.

10. Map these views to in apis/urls.py at valid endpoints.

11. Map 'apis.urls' in root urls.py and include appname other required packages to INSTALLED_APPS in settings.py.
    
11. Run the project on local server and use the APIs.
    ```
    python manage.py runserver
    ```
## Time spent on Project

Approximately 4-5 hours are spent on this project for final finish.

# Project Setup

1. Create virtualenv and activate it.
    ```
    virtualenv .venv

    source .venv/bin/activate
    ```

2. Clone the repository from github.
    ```
    git clone <gihub repo link>```

3. Go to projects root directry and install all requirements.
    ```
    pip install -r requirements.txt
    ```

4. Add the restored database (with indian bank details) configurations in settings.py.

5. Run the migrations commands.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run the project.
    ```
    python manage.py runserver
    ```

# Preview

Here is preview of APIs in this project. Can be accessed with this heroku url.
    [Indian banks API base url](https://indian-banks-137337d6b26f.herokuapp.com/)
