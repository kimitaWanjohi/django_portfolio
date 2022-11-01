from django.db import models

class Eductation(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.TextField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    screenshot = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    live_link = models.URLField(max_length=200)
    source_link = models.URLField(max_length=200)
    start_date = models.TextField()
    end_date = models.TextField()

    
    def __str__(self):
        return self.name



class Blogs(models.Model):
    title = models.CharField(max_length=255)
    blog_image_link = models.URLField(max_length=200)
    blog_link = models.URLField(max_length=200)
    brief_description = models.TextField()

    def __str__(self):
        return self.title