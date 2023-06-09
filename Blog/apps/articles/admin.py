from django.contrib import admin
from apps.articles.models import Articles


# admin.site.register(Articles)
@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','published','article_author')
    date_hierarchy = ('published')
    search_fields = ('title','article_author')