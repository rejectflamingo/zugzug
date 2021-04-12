from django.contrib import admin

# Register your models here.
from .models import Image
from .models import Studio
from .models import A2S

admin.site.register(Image)
admin.site.register(Studio)
admin.site.register(A2S)

