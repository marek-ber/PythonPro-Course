import random
from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Post, Category, Tag


class Command(BaseCommand):
    help = "Seed data - posts and categories"
    
    def handle(self, *args, **kwargs):
        fake = Faker("pl_PL")
        
        categories = ["Technologia", "Zdrowie", "Podróże", "Sport", "Kulinaria", "Polityka", "Newsy"]

        tags = ["Kobieta", "Mężczyzna", "Dziecko", "Pies", "Kot"]
        
        # for _ in range(10):
        #     category = Category.objects.create(
        #         name=fake.company()
        #     )
        #     categories.append(category)

        Post.objects.all().delete() 
        # DELETE FROM posts

        Category.objects.all().delete()
        Tag.objects.all().delete()

        created_tags = []
        for tag in tags:
            new_tag = Tag.objects.create(name=tag)
            created_tags.append(new_tag)


        created_categories = []
        for category in categories:
            new_category = Category.objects.create(name=category)
            created_categories.append(new_category)

        posts_created = 0
        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=" ".join(fake.paragraphs(nb=5)),
                category=random.choice(created_categories),  # Losowy autor z listy
                published_date=fake.date_time_this_year(),
                author=fake.name()
            )
            posts_created += 1
            
        print("Dodano")