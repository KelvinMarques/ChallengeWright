# Generated by Django 4.1 on 2022-08-19 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challengeWright_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='notelenovo',
            index_together={('name', 'description')},
        ),
    ]
