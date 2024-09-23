import os

from pyairtable import Table
from pyairtable.formulas import match
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AIRTABLE_TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("BASE_ID")


def create_record(table_name: str, record: dict) -> dict:
    table = Table(AIRTABLE_TOKEN, BASE_ID, table_name)
    result = table.create(record)
    return result


def get_record(table_name: str, filter: dict) -> dict:
    formula = match(filter)
    table = Table(AIRTABLE_TOKEN, BASE_ID, table_name)
    result = table.all(formula=formula)
    return result


def update_record(table_name: str, filter: dict, update: dict) -> dict:
    formula = match(filter)
    table = Table(AIRTABLE_TOKEN, BASE_ID, table_name)
    record = table.all(formula=formula)
    if len(record) > 0:
        id = record[0]["id"]
        result = table.update(id, update)
        return result
    else:
        return []


# result = create_record('users', {'username': 'x', 'password': 'y', 'status': 'inactive'})
# print(result)

# result = get_record('users', {'username': 'x'})
# print(result)

# result = update_record('users', {'username': 'x'}, {'username': 'xyz123'})
# print(result)
