from random import randint

from faker import Faker


def rand_ratio() -> tuple[int, int]:
    return randint(840, 900), randint(473, 573)  # noqa: S311


fake = Faker("pt_BR")


def make_recipe() -> dict:
    return {
        "title": fake.sentence(nb_words=6),
        "description": fake.sentence(nb_words=12),
        "preparation_time": fake.random_number(digits=2, fix_len=True),
        "preparation_time_unit": "Minutos",
        "servings": fake.random_number(digits=2, fix_len=True),
        "servings_unit": "Porção",
        "preparation_steps": fake.text(3000),
        "created_at": fake.date_time(),
        "author": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
        },
        "category": {"name": fake.word()},
        "cover": {
            "url": "https://loremflickr.com/%s/%s/food,cook" % rand_ratio(),
        },
    }


if __name__ == "__main__":
    from pprint import pprint as pp

    pp(make_recipe())  # noqa: T203
