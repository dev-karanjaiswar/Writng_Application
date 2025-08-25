from django.contrib import admin
from .models import BookCredential   # <-- make sure class name matches models.py

@admin.register(BookCredential)
class BookCredentialAdmin(admin.ModelAdmin):
    list_display = ('id','b_name','chapter','summary','ch_content','author','status')
    search_fields = ('b_name','chapter','author','status')
