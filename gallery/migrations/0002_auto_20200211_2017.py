# Generated by Django 3.0.3 on 2020-02-11 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Creator',
            new_name='Artist',
        ),
        migrations.RenameField(
            model_name='creation',
            old_name='creator',
            new_name='artist',
        ),
    ]
