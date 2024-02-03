from django.contrib import admin
from .models import Category,Post
# Register your models here.


#congigration of Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','post_id', 'url', 'image')

    search_fields = ('title',)
    list_filter = ('cat',)



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
