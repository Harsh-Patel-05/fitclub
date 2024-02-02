from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class deficiency(models.Model):
    de_type = models.CharField(max_length=30)

    def __str__(self):
        return self.de_type

class login(models.Model):
    de_id = models.ForeignKey(deficiency,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30,blank=True)
    phone_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    height = models.CharField(max_length=15)
    weight = models.CharField(max_length=15)
    address = models.TextField(default="")
    l_date = models.DateField(auto_now_add=True)
    age = models.IntegerField()
    role = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return self.email_id
    
class exercise(models.Model):
    de_id = models.ForeignKey(deficiency,on_delete=models.CASCADE)
    e_media = models.FileField(upload_to='photos')
    e_name = models.CharField(max_length=30)
    e_reps = models.TextField(default="")
    e_sets = models.TextField(default="")
    
class item(models.Model):
    i_name = models.CharField(max_length=30)
    i_photo = models.ImageField(upload_to='photos')
    i_desc = models.TextField()
    i_price = models.IntegerField()
    i_quantity = models.IntegerField()
    category = models.IntegerField()


    def item_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.i_photo.url))

    item_photo.allow_tags = True

    def __str__(self):
        return self.i_name