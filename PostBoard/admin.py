from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post,Author,Category,PostCategory
from markdownx.admin import MarkdownxModelAdmin


# Apply summernote to all TextField in model.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)