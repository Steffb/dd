from django.contrib import admin

# Register your models here.
from rss.models import Feed

admin.site.register(Feed)