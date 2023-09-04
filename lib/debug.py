from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Define your SQLite database URL here
DATABASE_URL = "sqlite:///mydatabase.db"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create the database tables (if not already created)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Get the first review from the database
first_review = session.query(Review).first()

if first_review:
    # Get the associated customer and restaurant for the first review
    customer = first_review.customer
    restaurant = first_review.restaurant

    # Print customer and restaurant information
    if customer and restaurant:
        print("Customer:", customer.first_name, customer.last_name)
        print("Restaurant:", restaurant.name)
    else:
        print("Customer or Restaurant not found for the first review.")
else:
    print("No reviews found in the database.")

# Retrieve and print all customers and their associated reviews
all_customers = session.query(Customer).all()
for customer in all_customers:
    print("Customer:", customer.first_name, customer.last_name)
    for review in customer.reviews:
        print("Review Rating:", review.rating)

# Retrieve and print all restaurants and their associated reviews
all_restaurants = session.query(Restaurant).all()
for restaurant in all_restaurants:
    print("Restaurant:", restaurant.name)
    for review in restaurant.reviews:
        print("Review Rating:", review.rating)
