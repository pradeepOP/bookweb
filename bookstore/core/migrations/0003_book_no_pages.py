# Generated by Django 4.2.3 on 2023-07-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='no_pages',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
