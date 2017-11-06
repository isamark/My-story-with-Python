from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name='名称',unique=True)
    address = models.CharField(max_length=128,verbose_name='地址')
    # 加一个字段操作者的目的是：为了只让出版社对象的编辑者有写的权限
    operator = models.ForeignKey("auth.User")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name


class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name='书名')
    publisher = models.ForeignKey("Publisher")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书"
        verbose_name_plural = verbose_name

