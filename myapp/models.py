from django.db import models


# Create your models here.

class Stu(models.Model):
    """自定义User表对应的model类"""
    # 自定义属性，默认主键自增id字段可不写
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)

    def __str__(self):
        return "%d:%s" % (self.id, self.name)

    class Meta:
        db_table = "stu"
