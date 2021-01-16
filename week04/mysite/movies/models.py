from django.db import models

# Create your models here.


class MovieInformation(models.Model):
    commit_id = models.IntegerField(null=True, name='评论id')
    short_comment = models.IntegerField(null=True, name='短评')
    star = models.IntegerField(null=True, name='星级')
    time = models.IntegerField(null=True, name='评论时间')
