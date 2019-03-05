from django.contrib import admin
from .models.hecho import Hecho
from .models.acontecimiento import Acontecimiento
from .models.lugar_hecho import LugarHecho
from .models.localizacion import Localizacion 


# Register your models here.
admin.site.register(Hecho)
admin.site.register(Acontecimiento)
admin.site.register(LugarHecho)
admin.site.register(Localizacion)