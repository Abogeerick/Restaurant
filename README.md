# Restaurant
## Overview
The Restaurant Review System is a Python application that manages and displays restaurant reviews. It utilizes SQLAlchemy for database interactions and provides a simple way to view customer reviews, associated restaurants, and customer information.

## Table of Contents
1. Getting Started
2. Prerequisites
3. Installation
4. Usage
5. Database Seeding
6. Contributing
7. License

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.
Prerequisites
Before you begin, ensure you have met the following requirements:

1. Python (version 3.8.10)
2. SQLAlchemy (version 1.4.41)
3. SQLite (version 3)
  
## Installation

To set up the project, follow these steps:
1.  Clone the repository:
```bash
    git clone https://github.com/yourusername/restaurant-review-system.git
```
2. Change to the project directory:
```bash
    cd restaurant-review-system
```
3. Install the required dependencies:
```bash
    pip install -r requirements.txt
```
## Usage

To run the Restaurant Review System, use the following command:
```bash
    python3 app.py
```
This will start the application, and you can interact with it via the command line.
Database Seeding
The project includes a script (seed_database.py) for populating the database with sample data. To seed the database, follow these steps:
Ensure you have set up the project as described in the Installation section.
Run the seeding script:
```bash
    python seed_database.py
```
This will add sample restaurants, customers, and reviews to the database.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise commit messages.
4. Push your changes to your forked repository.
5. Create a pull request to the original repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Erick Aboge
