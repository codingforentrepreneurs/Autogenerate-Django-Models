[![Autogenerate Django Models](https://static.codingforentrepreneurs.com/media/cfe-blog/auto-generate-django-models/Autogenerate_Django_Models.jpg)](https://www.codingforentrepreneurs.com/blog/auto-generate-django-models)

# Autogenerate Django Models

Learn how to take a scraped dataset and turn it into Django models using inspectdb. You can also use this method for legacy databases.

We'll use:
- Django (v2.2+)
- Jupyter
- SQLAlchemy
- Pandas
- sqlite3
- Python (v3+)

You can use this method to convert `SQLAlchemy`-managed models into `Django`-managed models as well. 


## How to use (after watching tutorial):

1. Download / Clone this [Repo](https://kirr.co/0bu8v5)
2. Activate a virtual environment `python3 -m venv .`
3. Run `pip install -r requirements.txt`
4. Run `jupyter notebook`
5. Navigate to `nbs/` and open `Autogen_Final.ipynb`
6. Run All Cells
7. Update `models.py` as you need related to the `python manage.py inspectdb --database lite` command.

> If you get a import error related to django, just do steps 2-4 in a new terminal / powershell.
