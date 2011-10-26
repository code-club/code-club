from foomash.models import *
from django.contrib import admin

class FooAdmin(admin.ModelAdmin):
	list_display = ('name', 'score')

admin.site.register(Foo, FooAdmin)
admin.site.register(Category)