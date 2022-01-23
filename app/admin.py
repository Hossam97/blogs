from django.contrib import admin
from .models import Articles
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author"]
    search_fields = ["id", "title", "author"]
    list_filter = ['author']
admin.site.register(Articles, ArticleAdmin)