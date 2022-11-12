from datetime import datetime

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