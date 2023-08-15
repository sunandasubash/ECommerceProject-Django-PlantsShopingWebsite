# Generated by Django 4.2.3 on 2023-07-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='img',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='products',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
