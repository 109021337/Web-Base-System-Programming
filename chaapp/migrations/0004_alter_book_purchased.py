# Generated by Django 4.0.3 on 2022-06-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaapp', '0003_book_author_book_isbn_book_press_book_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Purchased',
            field=models.IntegerField(null=True),
        ),
    ]