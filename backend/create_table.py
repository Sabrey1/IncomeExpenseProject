from database import Base, engine
import model  # IMPORTANT

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done!")