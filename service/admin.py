from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from service.models import (DishType,
                            Cook,
                            Ingredient,
                            Dish)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price", )
    list_filter = ("dish_type", "price", )
    search_fields = ("name", )


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (("Additional Info", {"fields": ("years_of_experience", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional Info", {"fields": (
        "first_name",
        "last_name",
        "years_of_experience", )}),)


admin.site.register(DishType)
admin.site.register(Ingredient)
