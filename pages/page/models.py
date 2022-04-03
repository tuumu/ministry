from __future__ import unicode_literals
from django.db import models 
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    author =  models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('devotion_detail', args=[str(self.id)])


    @property
    def snippet(self):
        return self.body[:400]

    def __str__(self):
        return str(self.title)

class Media(models.Model):
    name = models.CharField(max_length=150,null=True)
    description = models.TextField(blank=True,null=True)
    song= models.FileField(upload_to="videos")
    affiliate_url = models.CharField(blank=True, null=True,max_length=1000)
    created = models.DateTimeField(auto_now_add = True)
    author =  models.CharField(max_length=150,default="Bishop Francis Tumusiime")

    @property
    def snippet(self):
        return self.description[:400]

    def get_absolute_url(self):
        return reverse('sermon_detail', args=[str(self.id)])

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.name, self.created_on)


class Pics_day(models.Model):
    title = models.CharField(max_length=200,default='Ebenezer')
    body = models.TextField(max_length=200,default=False, blank=True, null=True)
    affiliate_url = models.SlugField(blank=True, null=True)
    image = models.ImageField(default=True,upload_to='static/img')
    uploaded = models.DateTimeField(auto_now_add=True,)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
                return self.title



class Whatusay(models.Model):
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(null=True)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Sermonsay(models.Model):
    comment = models.ForeignKey(Media,on_delete=models.CASCADE,related_name='sermon_comments')
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(null=True,blank=False)
    body = models.TextField(blank=False,default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

