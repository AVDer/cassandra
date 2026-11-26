import json
import os
import random
import sqlite3

from datetime import datetime, timedelta
from faker import Faker
from lorem_text import lorem

class TestDataFeeder:

    DB_FILE = 'data/work.db'
    NOTES_NUMBER = 100

    def __init__(self):
        self.accounts_number = 0

    def clear_database(self):
        connection = sqlite3.connect(self.DB_FILE)
        cursor = connection.cursor()

        tables = [table[0] for table in cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]

        for table in tables:
            cursor.execute(f"DELETE from {table}")

        connection.commit()
        connection.close()


    def add_accounts(self):
        global accounts_number
        with open(os.path.join(os.path.dirname(__file__), "test_accounts.json"), "r") as file:
            accounts = json.load(file)
        
        connection = sqlite3.connect(self.DB_FILE)
        cursor = connection.cursor()

        self.accounts_number = len(accounts)
        for account in accounts:
            cursor.execute(f"INSERT INTO accounts (name) VALUES ('{account["name"]}')")

        connection.commit()
        connection.close()

    def add_notes(self):
        connection = sqlite3.connect(self.DB_FILE)
        cursor = connection.cursor()
        faker = Faker()
        
        for _ in range(self.NOTES_NUMBER):
            note_title = lorem.words(3)
            note_text = lorem.paragraph()
            note_date = faker.date_between(datetime.now() - timedelta(days=30))
            cursor.execute(f"INSERT INTO notes (date, title, text, account_id) VALUES ('{note_date}', '{note_title}', '{note_text}', {random.randint(1, self.accounts_number)})")

        connection.commit()
        connection.close()

    def fill_with_data(self):
        self.clear_database()
        self.add_accounts()
        self.add_notes()

data_feeder = TestDataFeeder()
# data_feeder.fill_with_data()
data_feeder.clear_database()
