'''
ADMIN: Registrar modelos da aplicação na área administrativa.
'''

from django.contrib import admin
from .models import (

    Categoria,
 
)
admin.site.register([
    Categoria,
])
