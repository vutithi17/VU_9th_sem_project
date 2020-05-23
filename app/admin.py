# from django.contrib import admin
# from django.contrib.auth.models import Group

# # Register your models here.
# from .models import Contact

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'gender', 'email', 'info', 'phone','image',)
#     list_per_page = 10
#     search_fields = ('name', 'gender', 'email', 'info', 'phone',)
#     list_filter = ('gender','date_added')
#     list_editable =  ('info','email','phone','gender',)



# admin.site.register(Contact, ContactAdmin)

# admin.site.unregister(Group)

from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'gender', 'email', 'info', 'phone')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender','date_added')

admin.site.register(Contact, ContactAdmin)

# remove group
admin.site.unregister(Group)
