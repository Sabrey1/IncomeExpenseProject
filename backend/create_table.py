from database import Base, engine
import app.models.customer

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done!")