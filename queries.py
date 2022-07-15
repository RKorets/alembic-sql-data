from sqlalchemy import select, or_
from models import User, Email, Phone
from db import session


def add_phone(first_name: str, last_name: str, phone: str):
    search_queries = select(User).filter(User.first_name == f'{first_name}', User.last_name == f'{last_name}')
    user = session.execute(search_queries).scalar()
    if user:
        new_phone = Phone(
            user_id=user.id,
            phone=phone)
        session.add(new_phone)
        session.commit()
        print(f'Add phone {phone} for user {user.first_name} {user.last_name}')
    else:
        print('User not found')


def show_all_users():
    user_queries = select(User)
    result = session.execute(user_queries).scalars()
    for user in result:
        print(f'№{user.id}: {user.first_name} {user.last_name}')


def contact():
    user_contact = select(User).join(User.email).join(User.phone)
    result = session.execute(user_contact).scalars()
    for user in result:
        email = []
        phone = []
        for records in user.email:
            email.append(records.email)
        for records in user.phone:
            phone.append(records.phone)

        print(user.first_name, *phone, *email, sep=' | ')


def search_data():
    while True:
        search = input('\n\nInput search data (1 or more symbols: ')
        search_queries = select(User).join(Email).join(Phone)\
            .filter(or_(User.first_name.ilike(f'%{search}%'),
                    User.last_name.ilike(f'%{search}%'),
                    Email.email.ilike(f'%{search}%'),
                    User.address.ilike(f'%{search}%'),
                    Phone.phone.ilike(f'%{search}%')))
        result = session.execute(search_queries).scalars()
        rows = result.fetchall()
        if len(rows) == 0:
            print('No result')

        for user in rows:
            email = []
            phone = []
            for records in user.email:
                email.append(records.email)
            for records in user.phone:
                phone.append(records.phone)
            print(user.first_name, *phone, *email, user.address, sep=' | ')


if __name__ == '__main__':
    show_all_users()
    contact()
    search_data()
    add_phone('Олег', 'Сірченко', '00022-333-211')

