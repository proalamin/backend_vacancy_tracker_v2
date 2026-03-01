# Deploy Django Backend to PythonAnywhere

This project is ready to deploy on PythonAnywhere.

## 1) Create PythonAnywhere app

1. Sign in to PythonAnywhere.
2. Open **Web** tab -> **Add a new web app**.
3. Choose **Manual configuration**.
4. Select a Python version compatible with your `requirements.txt` (for `Django==6.0.2`, choose Python 3.12+).

## 2) Open a Bash console and set up project

Use your own username and paths in the commands below.

```bash
cd ~
git clone <your-repo-url>
cd backend_vacancy_tracker_v2
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 3) Set virtualenv in Web tab

In **Web** tab, set **Virtualenv** to:

- `/home/<username>/backend_vacancy_tracker_v2/.venv`

## 4) Set environment variables (Web app -> WSGI file)

In your PythonAnywhere WSGI file (for example `/var/www/<username>_pythonanywhere_com_wsgi.py`), add:

```python
import os
import sys

project_home = '/home/<username>/backend_vacancy_tracker_v2'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend_vac_tr_main.settings'
os.environ['DJANGO_SECRET_KEY'] = '<your-strong-secret-key>'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = '<username>.pythonanywhere.com'
os.environ['DJANGO_CSRF_TRUSTED_ORIGINS'] = 'https://<username>.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 5) Run migrations and collect static

From PythonAnywhere Bash console:

```bash
cd ~/backend_vacancy_tracker_v2
source .venv/bin/activate
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py createsuperuser
```

## 6) Configure static files in Web tab

Add static mapping:

- URL: `/static/`
- Directory: `/home/uualamin/backend_vacancy_tracker_v2/staticfiles`

## 7) Reload app

Go to **Web** tab and click **Reload**.

## 8) Quick verification

- Open `https://<username>.pythonanywhere.com/admin/`
- Open your API URLs (example: `/api/...`)

## Notes

- SQLite works for small/demo deployments. For production scale, move to MySQL/PostgreSQL.
- Keep `DJANGO_SECRET_KEY` private.
- If you get `DisallowedHost`, verify `DJANGO_ALLOWED_HOSTS` includes your exact domain.
