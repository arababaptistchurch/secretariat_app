from django.contrib import admin

# Register your models here.


from .models import *



class MemberAdmin(admin.ModelAdmin):
    fields = ['first_name', 'address', 'last_name']


admin.site.register(Members, MemberAdmin)
admin.site.register(Positions)
admin.site.register(AbcFamilies)