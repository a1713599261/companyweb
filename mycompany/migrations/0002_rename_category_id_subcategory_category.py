# Generated by Django 4.0.6 on 2022-08-28 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='category_id',
            new_name='category',
        ),
    ]
