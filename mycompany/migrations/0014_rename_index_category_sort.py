# Generated by Django 4.0.6 on 2022-08-31 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0013_alter_category_index'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='index',
            new_name='sort',
        ),
    ]