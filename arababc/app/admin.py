from django.contrib import admin

# Register your models here.

from app.models import Members, Positions, AbcFamilies


class PositionAdmin(admin.ModelAdmin):
    exclude = ('id',)


class ModelInline(admin.TabularInline):
    model = Positions


class MembersAdmin(admin.ModelAdmin):
    model = Members
    inlines = [
        ModelInline,
    ]

    exclude = ('id',)


# class PositionAdmin(admin.ModelAdmin):
#     list_display = getFieldsModel(Positions)
#     # prepopulated_fields = {"slug": ("first_name", "middle_name", "surname")}


# class PositionInline(admin.TabularInline):
#     model = Positions


# class MemberAdmin(admin.ModelAdmin):
#     list_display = getFieldsModel(Members)
#     prepopulated_fields = {"slug": ("first_name", "middle_name", "surname")}
#     exclude = ('id',)
#     inlines = [
#         PositionInline,
#     ]

admin.site.register(Members, MembersAdmin)
admin.site.register(Positions, PositionAdmin)
admin.site.register(AbcFamilies)
