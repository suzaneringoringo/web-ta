from django.contrib import admin

# Register your models here.

from .models import Verse
from .models import LinkType
from .models import Link

admin.site.register(Verse)
admin.site.register(LinkType)
admin.site.register(Link)