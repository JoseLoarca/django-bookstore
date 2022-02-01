from django.contrib import admin
from .models import Book, Author, Address, Country


# Register your models here

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'rating', 'author')
    list_display = ('title',)
    search_fields = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name',)
    search_fields = ('first_name',)


class AddressAdmin(admin.ModelAdmin):
    list_filter = ('street', 'postal_code', 'city')
    search_fields = ('street', 'city')
    list_display = ('street', 'postal_code', 'city')


class CountryAdmin(admin.ModelAdmin):
    list_filter = ('name', 'code')
    search_fields = ('name', 'code')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)