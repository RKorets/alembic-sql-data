from sqlalchemy import select, or_
from models import User, Contact
from db import session


def all_user():
    user_queries = select(User)
    result = session.execute(user_queries).scalars()
    for user in result:
        print(f'№{user.id}: {user.first_name} {user.last_name}')


def contact():
    user_contact = select(User).join(User.contacts)
    result = session.execute(user_contact).scalars()
    for user in result:
        for records in user.contacts:
            print(user.first_name, records.email, records.phone, records.address, sep=' | ')


def search_data():
    while True:
        search = input('\n\nInput search data (1 or more symbols: ')
        search_queries = select(User).join(Contact)\
            .filter(or_(User.first_name.ilike(f'%{search}%'),
                    User.last_name.ilike(f'%{search}%'),
                    Contact.email.ilike(f'%{search}%'),
                    Contact.address.ilike(f'%{search}%'),
                    Contact.phone.ilike(f'%{search}%')))
        result = session.execute(search_queries).scalars()
        rows = result.fetchall()
        if len(rows) == 0:
            print('No result')

        for user in rows:
            print(rows)
            for records in user.contacts:
                print(user.first_name, records.email, records.phone, records.address, sep=' | ')


if __name__ == '__main__':
    all_user()
    contact()
    search_data()
