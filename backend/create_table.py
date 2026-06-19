from database import Base, engine
# import app.models.role, app.models.customer, app.models.user
import app.models.payment_method

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done!")