from models import User, Email, Phone
from db import session
import faker


def create_user():
    fake_data = faker.Faker('uk-UA')
    for i in range(500):
        address = fake_data.address()
        if i % 2:
            first_name = fake_data.first_name_female()
            last_name = fake_data.last_name_female()
            user = User(first_name=first_name, last_name=last_name, address=address)
        else:
            first_name = fake_data.first_name_male()
            last_name = fake_data.last_name_male()
            user = User(first_name=first_name, last_name=last_name, address=address)
        session.add(user)
        session.commit()

        add_email = Email(
            user_id=user.id,
            email=fake_data.ascii_email())
        add_phone = Phone(
            user_id=user.id,
            phone=fake_data.phone_number())
        session.add(add_email)
        session.add(add_phone)
        session.commit()



if __name__ == '__main__':
    create_user()
