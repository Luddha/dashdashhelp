from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Wargames)
admin.site.register(WG_DOCS)
admin.site.register(WG_VMS)