# Testing GeoDjango
Pruebas sobre GeoDjango y postgis

Siguiendo el tutorial en  
https://docs.djangoproject.com/es/1.9/ref/contrib/gis/

### Instalar

```
# Crear entorno
mkvirtualenv geodjango --python=python3
pip install -r requirements.txt
# crear una base de datos en postres segun las instrucciones
python manage.py migrate
python manage.py loaddata fixtures.json
```

### Editar GIS directo desde el admin:  
Hay widgets especiales para administrar estos modelos  
```
from django.contrib.gis import admin
```

Puede usarse el estándar _GeoModelAdmin_  
```
admin.site.register(WorldBorder, admin.GeoModelAdmin)
```
O el especial de _OpenStreetMaps_  
```
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
```

#### Imágenes

![Imagen1](https://github.com/avdata99/testing-GeoDjango/blob/master/Selección_082.png?raw=true)
![Imagen2](https://github.com/avdata99/testing-GeoDjango/blob/master/Selección_083.png?raw=true)
