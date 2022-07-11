from models import User, Contact
from db import session
import faker


def create_user():
    fake_data = faker.Faker('uk-UA')
    for i in range(500):
        if i % 2:
            user = User(first_name=fake_data.first_name_female(), last_name=fake_data.last_name_female())
        else:
            user = User(first_name=fake_data.first_name_male(), last_name=fake_data.last_name_male())
        session.add(user)
        session.commit()

        contact = Contact(
            user_id=user.id,
            address=fake_data.address(),
            phone=fake_data.phone_number(),
            email=fake_data.ascii_email())
        session.add(contact)
    session.commit()


if __name__ == '__main__':
    create_user()
