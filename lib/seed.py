from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review




def seed_database():
    # Create a database engine
    engine = create_engine("sqlite:///mydatabase.db")  
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add your data to the database
    restaurant1 = Restaurant(name="Restaurant 1", price=2)
    restaurant2 = Restaurant(name="Restaurant 2", price=3)

    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")

    review1 = Review(rating=4, restaurant_id=restaurant1.id, customer_id=customer1.id)
    review2 = Review(rating=5, restaurant_id=restaurant2.id, customer_id=customer2.id)

    # Add instances to the session
    session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

    # Commit the changes to the database
    session.commit()

if __name__ == "__main__":
    seed_database()
