import json

import requests
from faker import Faker

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"


def getAuthToken():
    r = requests.post(f"{APIHOST}/api/v1/loginViaBasic", auth=(LOGIN, PASSWORD))
    if r.status_code == 200:
        return r.json()["token"]
    raise Exception(f"Status code {r.status_code} en tekst {r.text} bij het inloggen.")


def getBooks():
    r = requests.get(f"{APIHOST}/api/v1/books")
    print("GET /books status:", r.status_code)
    return r.json()


def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books",
        headers={"Content-type": "application/json", "X-API-Key": apiKey},
        data=json.dumps(book),
    )
    if r.status_code == 200:
        print(f"Boek {book['id']} toegevoegd: {book['title']}")
    else:
        raise Exception(f"Error code {r.status_code} en tekst {r.text} bij boek {book}.")


apiKey = getAuthToken()
print("Token ontvangen:", apiKey)

fake = Faker()
for i in range(90, 100):
    book = {"id": i, "title": fake.catch_phrase(), "author": fake.name(), "isbn": fake.isbn13()}
    addBook(book, apiKey)

boeken = getBooks()
print("Aantal boeken nu:", len(boeken))
for boek in boeken[-10:]:
    print(boek["id"], "-", boek["title"], "-", boek["author"])
