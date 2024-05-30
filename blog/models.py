from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=400)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=20)
    wechat = models.CharField(max_length=200)

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=200000)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    star = models.IntegerField(default=0)
    tag = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    last_edit_date = models.DateTimeField("date last edit")