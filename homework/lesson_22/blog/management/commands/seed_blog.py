import random

from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = 'Seeds the blog with sample categories, tags and posts.'

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

        categories = [Category.objects.create(name=name) for name in category_names]
        tags = [Tag.objects.create(name=name) for name in tag_names]

        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content='\n\n'.join(fake.paragraphs(nb=5)),
                category=random.choice(categories),
                status='published',
            )
            post.tags.set(random.sample(tags, random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS('Utworzono 100 postów, kategorie i tagi.'))
