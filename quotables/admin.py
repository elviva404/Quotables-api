from django.contrib import admin
from quotables.models import User

# Register your models here.
admin.site.register(User)

admin.AdminSite.site_header = "Quotables Admin"

