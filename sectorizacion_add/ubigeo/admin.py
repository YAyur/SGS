from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from .models import Department, Province, District

#admin.site.register(Department)
#admin.site.register(Province)
#admin.site.register(District)




@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display=('name',)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    fields = ('name', 'parent')
    list_display=('name', 'parent')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    fields = ('name', 'parent')
    list_display=('name', 'parent')

