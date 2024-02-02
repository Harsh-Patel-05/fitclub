from django.contrib import admin
from myapp.forms import displayform
from .models import login,deficiency,item

# Register your models here.
class showdeficiency(admin.ModelAdmin):
    list_display = ["de_type"]
admin.site.register(deficiency,showdeficiency)

class showlogin(admin.ModelAdmin):
    form = displayform
    list_display = ("de_id","firstname","lastname","password","email_id","phone_no","gender","height","weight","age","role","status","address","l_date")
admin.site.register(login,showlogin)

class showitem(admin.ModelAdmin):
    list_display = ("category","item_photo","i_name","i_desc","i_price","i_quantity")
admin.site.register(item,showitem)