from django.db import models
from utils.base_model import BaseModel
# from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

# Create your models here.

# 栏目表
class Category(BaseModel):
    title = models.CharField(max_length=25, null=False, verbose_name='栏目标题')
    tag_title = models.CharField(max_length=20, default='', verbose_name='标签标题', null=True, blank=True)
    tag_des = models.CharField(max_length=256, default='', verbose_name='标签标题下的文字介绍', null=True, blank=True)
    show_image_pc_in = models.ImageField(upload_to='images', default='', verbose_name='内电脑端缩略图')
    show_image_m_in = models.ImageField(upload_to='images', default='', verbose_name='内手机端缩略图')
    show_image_pc_index = models.ImageField(upload_to='images', default='', verbose_name='外电脑端缩略图')
    show_image_m_index = models.ImageField(upload_to='images', default='', verbose_name='外手机端缩略图', null=True, blank=True)
    sort = models.IntegerField(default=0, verbose_name='排序-值越大越靠前')

    class Meta:
        db_table = 'category'
        verbose_name = '栏目表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=False, verbose_name='子栏目标题')
    # 富文本类型:带有格式的文本
    detail = RichTextField(blank=True, verbose_name='栏目文章详情')

    class Meta:
        db_table = 'sub_category'
        verbose_name = '子栏目表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(BaseModel):
    # image_path = models.CharField(max_length=60, null=False)
    banner_show_photo = models.ImageField(upload_to='images', default='', verbose_name='广告展示图')

    class Meta:
        db_table = 'banner'
        verbose_name = 'banner图'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.banner_m_photo + self.banner_m_photo

class CompanyContact(BaseModel):
    phone = models.CharField(max_length=11, null=False)
    email = models.CharField(max_length=20, null=False)
    # logo_path = models.CharField(max_length=60, null=False)
    logo_picture = models.ImageField(upload_to='images', default='', blank=True, null=True)

    class Meta:
        db_table = 'company_contact'
        verbose_name = '公司信息表'
        verbose_name_plural = verbose_name
