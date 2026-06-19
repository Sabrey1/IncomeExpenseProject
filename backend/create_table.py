from database import Base, engine
import app.models.role, app.models.customer, app.models.user,app.models.payment_method, app.models.exchange_rate, app.models.currency, app.models.expense_type, app.models.expense, app.models.income_type, app.models.income

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done!")