# Generated by Django 4.0.6 on 2022-08-31 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0008_category_tag_des_category_tag_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='show_image_m_index',
            field=models.ImageField(default='', null=True, upload_to='images', verbose_name='外手机端缩略图'),
        ),
        migrations.AlterField(
            model_name='category',
            name='tag_des',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='标签标题下的文字介绍'),
        ),
        migrations.AlterField(
            model_name='category',
            name='tag_title',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='标签标题'),
        ),
    ]
