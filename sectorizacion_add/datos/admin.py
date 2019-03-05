from django.contrib import admin

# Register your models here.
from .models.persona import Persona
from .models.policia import Policia
from .models.turista import Turista


# Register your models here.
admin.site.register(Persona)
admin.site.register(Policia)
admin.site.register(Turista)
