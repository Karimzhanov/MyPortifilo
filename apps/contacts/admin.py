from django.contrib import admin
from .models import Contacts, PageContact

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'service', 'subject')
    list_filter = ('name',)
    search_fields = ('name', 'number', 'email', 'subject')

class PageContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'subject', 'message')
    list_filter = ('name',)
    search_fields = ('name', 'number', 'email', 'subject', 'message')

admin.site.register(Contacts, ContactsAdmin)
admin.site.register(PageContact, PageContactAdmin)
