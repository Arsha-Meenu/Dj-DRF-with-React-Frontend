from django.contrib import admin
from app.articles.models import Articles


# admin.site.register(Articles)
@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','published','author')
    date_hierarchy = ('published')
    search_fields = ('title','author')