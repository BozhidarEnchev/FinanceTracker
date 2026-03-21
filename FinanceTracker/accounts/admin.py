from django.contrib import admin

from FinanceTracker.accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass
