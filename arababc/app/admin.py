from django.contrib import admin

# Register your models here.


from app.models import Members, Positions, AbcFamilies


class MemberAdmin(admin.ModelAdmin):
    fields = ['first_name', 'residential_address', 'surname']


admin.site.register(Members, MemberAdmin)
admin.site.register(Positions)
admin.site.register(AbcFamilies)
