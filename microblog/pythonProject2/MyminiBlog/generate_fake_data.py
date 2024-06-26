import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyminiBlog.settings')

django.setup()

from faker import Faker
from random import choice
from django.contrib.auth.models import User
from Myblog.models import Post

fake = Faker('ru_RU')


def generate_fake_user():
    username = fake.user_name()
    email = fake.email()
    password = 'password123'
    user = User.objects.create_user(username=username, email=email, password=password)
    return user


def generate_fake_post(author):
    title = fake.sentence(nb_words=6)
    description = fake.text(max_nb_chars=2000)
    data = fake.date()
    post = Post.objects.create(
        title=title,
        description=description,
        author=author,
        data=data
    )
    return post


def generate_fake_data(num_users, num_posts):
    users = []
    for _ in range(num_users):
        user = generate_fake_user()
        users.append(user)

    for _ in range(num_posts):
        author = choice(users)
        generate_fake_post(author)


if __name__ == '__main__':
    NUM_USERS = 5
    NUM_POSTS = 10
    generate_fake_data(NUM_USERS, NUM_POSTS)
    print(f'Generated {NUM_POSTS} post for {NUM_USERS} users.')
