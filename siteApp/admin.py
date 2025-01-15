from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ContactMessage, Stage, Formation, Actualite


admin.site.register(ContactMessage)
admin.site.register(Stage)
admin.site.register(Formation)
admin.site.register(Actualite)

