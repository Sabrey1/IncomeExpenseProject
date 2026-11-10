from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from app.core.dependencies import get_current_user
from app.routers import user, customer, roles, currency, payment_method, expense_type, expense, income_type, income, exchange_rate, auth

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = "/v1/api"

app.include_router(auth.router, prefix=f"{API_PREFIX}/login", tags=["Authentication"])


protected_routers = [
    (user.router, "users", "Users"),
    (customer.router, "customers", "Customers"),
    (roles.router, "roles", "Roles"),
    (currency.router, "currencies", "Currencies"),
    (payment_method.router, "payment-methods", "Payment Methods"),
    (expense_type.router, "expense-types", "Expense Types"),
    (expense.router, "expenses", "Expenses"),
    (income_type.router, "income-types", "Income Types"),
    (income.router, "incomes", "Incomes"),
    (exchange_rate.router, "exchange-rates", "Exchange Rates"),
]

for router, path, tag in protected_routers:
    app.include_router(
        router,
        prefix=f"{API_PREFIX}/{path}",
        tags=[tag],
        dependencies=[Depends(get_current_user)]
    )