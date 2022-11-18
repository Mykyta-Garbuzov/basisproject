from flask import abort
from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema


def read_all():
    people = Person.query.all()
    return people_schema.dump(people)


def create(person):
    name = person.get("name")
    existing_person = Person.query.filter(Person.name == name).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {name} already exists",
        )


def read_one(surname):
    person = Person.query.filter(Person.surname == surname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {surname} not found"
        )


def update(surname, person):
    existing_person = Person.query.filter(
        Person.surname == surname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.name = update_person.name
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
            404,
            f"Person with last surname {surname} not found")


def delete(surname):
    existing_person = Person.query.filter(
        Person.surname == surname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{surname} successfully deleted", 200)
    else:
        abort(
            404,
            f"Person with last name {surname} not found"
        )
