# FinanceTracker
Backend application for managing transactions, budgets and financial accounts. The idea of the project is to be selfhostable and reliable.

## Features
- JWT Authentication
- User data isolation
- Category-based financial logic
- Automatic account balance updates
- Monthly budgeting
- API documentation with Swagger (drf-spectacular)


## Business Logic
1. The user registers a transaction that has a category and a source/destination financial account.
2. Depending on the category of the transaction, its amount is added to the financial account and the user's total amount.

## Running the project
Clone the repo, install the requirements and run the server.
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API documentation
Interactive API documentation is available at:
- Swagger UI: `/api/schema/swagger-ui/`
- ReDoc: `/api/schema/redoc/`

## Tech Stack
- Python
- Django and Django REST Framework
- PostgreSQL
- drf-spectacular

## Future Development
- [ ] Frontend
- [ ] Budget settings and logic inspired by the 50/30/20 rule
- [ ] Analytics (reports, charts)
- [ ] AI-based expense categorization
- [ ] Recurring transactions

## Status
Work in progress - Many of the features might not work as intended
