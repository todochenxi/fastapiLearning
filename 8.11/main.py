from datetime import date

from pydantic import BaseModel


def main(user_id: str):
    return user_id


class User(BaseModel):
    id: int
    name: str
    joined: date


my_user: User = User(id=3, name="chenxi", joined="2023-8-11")
second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2023-8-11",
}
my_second_user: User = User(**second_user_data)
print(my_second_user)
