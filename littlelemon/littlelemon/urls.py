from django.contrib import admin

from django.urls import path, include

import restaurant 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restaurant.urls')),
    path('restaurant/booking/', include(restaurant.urls.router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
   
]
