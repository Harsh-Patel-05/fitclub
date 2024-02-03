from django.db import models
from django.utils.safestring import mark_safe

FOOD_OPT=(
    ("Vegetarian","Vegetarian"),
    ("Non-Vegetarian","Non-Vegetarian")

)
WEIGHT_OPT=(
    ("Weight-gain","Weight-gain"),
    ("Weight-loose","Weight-loose")
)

TIME_OPT=(
    ("Breakfast","Breakfast"),
    ("Lunch","Lunch"),
    ("Dinner","Dinner")
)

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

class diet(models.Model):
    de_id = models.ForeignKey(deficiency,on_delete=models.CASCADE)
    d_name = models.CharField(max_length=30)
    d_name2 = models.CharField(max_length=30)
    food_type = models.CharField(choices=FOOD_OPT,max_length=30)
    weight_type = models.CharField(choices=WEIGHT_OPT,max_length=30)
    time_type = models.CharField(choices=TIME_OPT,max_length=30)
    calories = models.CharField(max_length=30)
    calories2 = models.CharField(max_length=30)
    day = models.IntegerField()
    diet_time = models.CharField(max_length=30)


class blog(models.Model):
    l_id = models.ForeignKey(login,on_delete=models.CASCADE)
    wr_name = models.CharField(max_length=50)
    b_name = models.CharField(max_length=70)
    b_desc1 = models.TextField(default="")
    b_desc2 = models.TextField(default="")
    b_media = models.ImageField(upload_to='photos')

    def blog_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.b_media.url))

    blog_photo.allow_tags = True


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

class order(models.Model):
    i_id = models.ForeignKey(item,on_delete=models.CASCADE)
    loginid = models.ForeignKey(login,on_delete=models.CASCADE)
    o_quantity = models.IntegerField()
    total = models.IntegerField()
    o_date_time = models.DateTimeField(auto_now_add=True,editable=False)
    oid = models.IntegerField(null=True)
    ostatus = models.IntegerField(null=True)

class placeorder(models.Model):
    loginid = models.ForeignKey(login, on_delete=models.CASCADE)
    tamount = models.IntegerField(null=True)
    o_date_time = models.DateTimeField(auto_now_add=True,editable=False)

class feedback(models.Model):
    l_id = models.ForeignKey(login,on_delete=models.CASCADE)
    review = models.IntegerField()
    comment = models.TextField()
    f_date_time = models.DateTimeField(auto_now_add=True,editable=False)

class contactus(models.Model):
    name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30,blank=True)
    subject = models.TextField()
    message = models.TextField()

