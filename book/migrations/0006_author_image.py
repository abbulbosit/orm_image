# Generated by Django 5.0.6 on 2024-07-05 11:36

import book.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(default=1, upload_to=book.helpers.Change_name.change),
            preserve_default=False,
        ),
    ]
