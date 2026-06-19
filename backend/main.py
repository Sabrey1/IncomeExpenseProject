from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base

from app.routers import user, customer, roles, currency, payment_method, expense_type, expense, income_type, income, exchange_rate

import app.models.user, app.models.customer, app.models.role, app.models.currency, app.models.payment_method, app.models.expense_type, app.models.expense, app.models.income_type, app.models.income, app.models.exchange_rate

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(customer.router, prefix="/customers", tags=["Customers"])
app.include_router(roles.router, prefix="/roles", tags=["Roles"])
app.include_router(currency.router, prefix="/currencies", tags=["Currencies"])
app.include_router(payment_method.router, prefix="/payment-methods", tags=["Payment Methods"])
app.include_router(expense_type.router, prefix="/expense-types", tags=["Expense Types"])
app.include_router(expense.router, prefix="/expenses", tags=["Expenses"])
app.include_router(income_type.router, prefix="/income-types", tags=["Income Types"])
app.include_router(income.router, prefix="/incomes", tags=["Incomes"])
app.include_router(exchange_rate.router, prefix="/exchange-rates", tags=["Exchange Rates"])