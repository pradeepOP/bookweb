# Generated by Django 4.2.3 on 2023-07-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='default.jpg', upload_to='book_covers'),
        ),
    ]