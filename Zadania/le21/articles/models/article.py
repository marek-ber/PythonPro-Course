from django.db import models as m


class Article(m.Model):
    title = m.CharField(max_length=200)
    content = m.TextField()
    pub_date = m.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


def get_all():
    return Article.objects.all()


def create(title, content):
    # a = Article(title=title, content=content)
    # a.save()

    ar = Article.objects.create(title=title, content=content)
    print("utworzono artykuł django")
    return ar
