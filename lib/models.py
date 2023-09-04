# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func 

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    # Define the one-to-many relationship with Review
    reviews = relationship("Review", back_populates="restaurant")

    @classmethod
    def fanciest(cls, session):
        # Use SQLAlchemy's func.max() to find the restaurant with the highest price
        max_price = session.query(func.max(cls.price)).scalar()
        return session.query(cls).filter_by(price=max_price).first()

    def all_reviews(self, session):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        formatted_reviews = []
        for review in reviews:
            formatted_review = f"Review for {self.name} by {review.customer.full_name()}: {review.rating} stars."
            formatted_reviews.append(formatted_review)
        return formatted_reviews

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define the one-to-many relationship with Review
    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, session):
        reviews = session.query(Review).filter_by(customer_id=self.id).all()
        if not reviews:
            return None
        highest_rating = max(reviews, key=lambda x: x.rating)
        return highest_rating.restaurant

    def add_review(self, session, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, session, restaurant):
        reviews_to_delete = session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant.id).all()
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)  # Add the rating attribute as an example
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars."