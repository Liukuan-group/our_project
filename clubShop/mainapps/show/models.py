import os
import uuid

from django.db import models
from db.base_model import BaseModel
from DjangoUeditor.models import UEditorField
# Create your models here.

class Class(BaseModel):
    name = models.CharField(max_length=20, verbose_name='课程名称')
    desc = models.CharField(max_length=100, verbose_name='课程描述')
    image = models.ImageField(upload_to='class', verbose_name='课程图片')
    phone = models.CharField(max_length=15, verbose_name='咨询电话')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_class'
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class article(BaseModel):
    '''文章模型类'''
    title = models.CharField(max_length=50, verbose_name='标题')
    content = UEditorField(verbose_name='内容',
                           blank=True,
                           width=640,height=480,
                           imagePath='ueditor/imgs/',
                           filePath='ueditor/files/',
                           toolbars='full')

    date = models.DateTimeField(null=True, verbose_name='日期',auto_now_add=True)
    image = models.ImageField(upload_to='article', verbose_name='文章图片',blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.image.name) < 30:
            self.image.name = str(uuid.uuid4()).replace('-', '')+ os.path.splitext(self.image.name)[-1]
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name