from django.urls import include, path
from django.contrib import admin


app_name = "crud"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls', namespace='crud')),
]
