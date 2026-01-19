from django.contrib import admin
from memories.models import Memory
from django.contrib.auth.models import User


class MemoryAdmin(admin.ModelAdmin):
    list_display=('id','title','body', 'author', 'created_at')
    prepopulated_fields={'slug':('title',)}
    search_fields=('id', 'title', 'author__username')
    list_editable=('title',)

admin.site.register(Memory, MemoryAdmin)