from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review
import random

def seed_database():
    # Define your SQLite database URL here
    DATABASE_URL = "sqlite:///mydatabase.db"

    # Create a database engine
    engine = create_engine(DATABASE_URL)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add your data to the database
    restaurant1 = Restaurant(name="Restaurant 1", price=2)
    restaurant2 = Restaurant(name="Restaurant 2", price=3)

    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")

    # Generate and insert 50 random reviews
    for _ in range(50):
        rating = random.randint(1, 5)  # Generate a random rating between 1 and 5
        # Choose a random restaurant and customer for the review
        restaurant = random.choice([restaurant1, restaurant2])
        customer = random.choice([customer1, customer2])
        review = Review(rating=rating, restaurant_id=restaurant.id, customer_id=customer.id)
        session.add(review)

    # Commit the changes to the database
    session.commit()

if __name__ == "__main__":
    seed_database()
