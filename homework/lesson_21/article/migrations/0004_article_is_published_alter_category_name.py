# Generated manually for lesson 21 corrections

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_rename_category_id_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
