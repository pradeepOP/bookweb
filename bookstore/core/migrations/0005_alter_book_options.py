# Generated by Django 4.2.3 on 2023-07-14 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_book_created_book_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
