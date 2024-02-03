from django.contrib import admin
from .models import login,deficiency,exercise,diet,blog,item,order,feedback,contactus,placeorder
from .forms import displayform

# Register your models here.
class showdeficiency(admin.ModelAdmin):
    list_display = ["de_type"]
admin.site.register(deficiency,showdeficiency)

class showlogin(admin.ModelAdmin):
    form = displayform
    list_display = ("de_id","firstname","lastname","password","email_id","phone_no","gender","height","weight","age","role","status","address","l_date")
admin.site.register(login,showlogin)

class showexercise(admin.ModelAdmin):
    list_display = ("de_id","e_name","e_media")
admin.site.register(exercise,showexercise)

class showdiet(admin.ModelAdmin):
    list_display = ("de_id","d_name","d_name2","food_type","weight_type","time_type","calories","calories2","day","diet_time")
admin.site.register(diet,showdiet)

class showblog(admin.ModelAdmin):
    list_display = ("l_id","wr_name","b_name","b_desc1","b_desc2","b_media")
admin.site.register(blog,showblog)

class showitem(admin.ModelAdmin):
    list_display = ("category","item_photo","i_name","i_desc","i_price","i_quantity")
admin.site.register(item,showitem)

class showorder(admin.ModelAdmin):
    list_display = ("i_id","o_quantity","loginid","total","o_date_time")
admin.site.register(order,showorder)

class showfeedback(admin.ModelAdmin):
    list_display = ("l_id","review","comment","f_date_time")
admin.site.register(feedback,showfeedback)

class showcontactus(admin.ModelAdmin):
    list_display = ("name","email_id","subject","message")
admin.site.register(contactus,showcontactus)

class showplaceorder(admin.ModelAdmin):
    list_display = ("loginid","o_date_time","tamount")
admin.site.register(placeorder,showplaceorder)