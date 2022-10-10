# Generated by Django 4.0.6 on 2022-08-31 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0007_remove_banner_banner_m_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tag_des',
            field=models.CharField(default='', max_length=256, verbose_name='标签标题下的文字介绍'),
        ),
        migrations.AddField(
            model_name='category',
            name='tag_title',
            field=models.CharField(default='', max_length=20, verbose_name='标签标题'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=25, verbose_name='栏目标题'),
        ),
    ]