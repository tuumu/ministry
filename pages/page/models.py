from django.db import models
from datetime import * 
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    author =  models.CharField(max_length=150,default="Bishop Francis Tumusiime")

    def __str__(self):
        return str(self.title)

    @property
    def snippet(self):
        return self.body[:700]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class AllSongs(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    song= models.FileField(upload_to="videos")
    description = models.TextField(blank=True)
    affiliate_url = models.SlugField(blank=True, null=True)
    release = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sermon_detail', args=[str(self.id)])



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    chat = models.ForeignKey(AllSongs,on_delete=models.CASCADE,related_name='chat',null=False,default=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


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

class Scripture(models.Model):
    title = models.CharField(max_length=200,default='The finished work of christ')
    body = models.TextField(max_length=200,default=False, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
                return self.title

class quote(models.Model):
    name = models.CharField(max_length=200,default='Faith,Hope and Love')
    body = models.TextField(max_length=200,default=False, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
                return self.name

class Notes(models.Model):
    title = models.CharField(max_length=200,default='The perfection of God')
    body = models.TextField(max_length=200,default=False, blank=True, null=True)
    date_noted = models.DateTimeField(auto_now_add=True)


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
    comment = models.ForeignKey(AllSongs,on_delete=models.CASCADE,related_name='sermon_comments')
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(null=True,blank=False)
    body = models.TextField(blank=False,default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Ad(models.Model):
    title = models.CharField(max_length=200,blank=True)
    body = models.TextField(max_length=200,default=False, blank=True, null=True)
    
    def __str__(self):
                return self.title