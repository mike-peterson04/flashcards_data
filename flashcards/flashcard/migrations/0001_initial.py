# Generated by Django 3.1.8 on 2021-06-02 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=50)),
                ('definition', models.CharField(max_length=50)),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcard.collection')),
            ],
        ),
    ]
