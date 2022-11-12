from datetime import datetime
from flask import abort
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Germany": {
        "name": "Agata",
        "surname": "Hall",
        "timestamp": get_timestamp(),
    },
    "Belgium ": {
        "name": "James",
        "surname": "Deleu",
        "timestamp": get_timestamp(),
    },
    "Ukraine": {
        "name": "Mykyta",
        "surname": "Garbuzov",
        "timestamp": get_timestamp(),
    }
}


def read_all():
    return list(PEOPLE.values())

def create(person):
    name = person.get("name")
    surname = person.get("surname", "")

    if name and name not in PEOPLE:
        PEOPLE[name] = {
            "name": name,
            "surname": surname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[name], 201
    else:
        abort(
            406,
            f"Person with last name {name} already exists",
        )

def read_one(surname):
    if surname in PEOPLE:
        return PEOPLE.get(surname)
    else:
        abort(
            404, f"Person with last name {surname} not found"
        )

def update(name, person):
    if name in PEOPLE:
        PEOPLE[name]["surname"] = person.get("surname", PEOPLE[name]["surname"])
        PEOPLE[name]["timestamp"] = get_timestamp()
        return PEOPLE[name]
    else:
        abort(
            404,
            f"Person with last name {name} not found")


def delete(surname):
    if surname in PEOPLE:
        del PEOPLE[surname]
        return make_response(
            f"{surname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {surname} not found"
        )