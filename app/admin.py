from django.contrib import admin
from app.models import Event, Member,User,People,Contact

from import_export.admin import ImportExportModelAdmin

# Register your models here.


# admin.site.register(Event)
admin.site.register(Member)

#admin.site.register(People)

# admin.site.unregister(Group)


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'is_superuser')

    search_fields = ('email',)

    list_filter = ('date_joined',)
    date_hierarchy = 'date_joined'


@admin.register(Event)
class EventModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'description', 'location', 'price']
    list_filter = ['title', 'created_at', 'price']
    search_fields = ['title', 'location']

@admin.register(People)
class PeopleModelAdmin(admin.ModelAdmin):
    list_display = ['email','created_at','updated_at']
    search_fields = ['email']
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','message']
    search_fields = ['email','full_name']
    list_filter = ['created_at']