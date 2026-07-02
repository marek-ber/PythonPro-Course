import random

from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = 'Tworzy przykładowe kategorie, tagi i posty.'

    def handle(self, *args, **kwargs):
        fake = Faker('pl_PL')

        self.stdout.write('Usuwanie starych danych...')
        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()

        category_names = [
            'Technologia',
            'Podróże',
            'Kulinaria',
            'Sport',
            'Zdrowie',
            'Programowanie',
            'Motoryzacja',
        ]

        tag_names = [
            'django',
            'python',
            'ai',
            'poradnik',
            'recenzja',
            'news',
            'praktyka',
            'backend',
            'webdev',
            'tutorial',
        ]

        categories = []
        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)

        tags = []
        for name in tag_names:
            tag = Tag.objects.create(name=name)
            tags.append(tag)

        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content='\n\n'.join(fake.paragraphs(nb=5)),
                category=random.choice(categories),
            )
            post.tags.set(random.sample(tags, random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS('Utworzono 100 postów, kategorie i tagi.'))
