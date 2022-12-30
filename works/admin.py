from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Part

class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    mptt_indent_field = "name"
    list_display = ('code', 'name', )   


admin.site.register(Part, CustomMPTTModelAdmin)    