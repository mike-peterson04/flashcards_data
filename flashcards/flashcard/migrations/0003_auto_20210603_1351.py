# Generated by Django 3.1.8 on 2021-06-03 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_auto_20210603_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='collection_id',
            new_name='collection',
        ),
    ]
