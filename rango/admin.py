from rango.models import UserProfile
from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register the models with their respective admins

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
