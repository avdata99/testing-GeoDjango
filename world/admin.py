from django.contrib.gis import admin
from .models import *

# admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Zipcode, admin.GeoModelAdmin)
admin.site.register(Address, admin.GeoModelAdmin)
admin.site.register(Elevation, admin.GeoModelAdmin)
admin.site.register(SouthTexasCity, admin.GeoModelAdmin)
