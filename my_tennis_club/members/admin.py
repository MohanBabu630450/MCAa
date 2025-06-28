from django.contrib import admin
from .models import Member
class MemberAdmin(admin.ModelAdmin):
    list_displa=('firstname','lastname','joined date')

admin.site.register(Member)

# Register your models here.
