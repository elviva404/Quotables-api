from django.contrib import admin
from quotables.models import User, Artist, Mood, Category, Quote

# Register your models here.
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Mood)
admin.site.register(Category)
admin.site.register(Quote)

admin.AdminSite.site_header = "Quotables Admin"

