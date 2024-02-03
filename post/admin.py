from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin


from post.models import Income, Expense


# class CustomUserAdmin(UserAdmin):
#     pass

admin.site.register(Income)
admin.site.register(Expense)


