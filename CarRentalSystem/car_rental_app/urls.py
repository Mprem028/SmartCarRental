"""car_rental_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

# from django.urls import path, include
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
# from system.views import admin_car_list, admin_msg, order_list, car_created, order_update, order_delete, msg_delete
# from accounts.views import (login_view, register_view, logout_view)

# urlpatterns = [
#     path(r'^admin/', admin.site.urls),
#     path(r'^$', admin_car_list, name='adminIndex'),
#     path(r'^listOrder/$', order_list, name = "order_list"),
#     path(r'^(?P<id>\d+)/editOrder/$', order_update, name = "order_edit"),
#     path(r'^(?P<id>\d+)/deleteOrder/$', order_delete, name = "order_delete"),
#     path(r'^create/$', car_created, name = "car_create"),
#     path(r'^message/$', admin_msg, name='message'),
#     path(r'^(?P<id>\d+)/deletemsg/$', msg_delete, name = "msg_delete"),
#     path(r'^car/', include('system.urls')),
#     path(r'^login/', login_view, name='login'),
#     path(r'^logout/', logout_view, name='logout'),
#     path(r'^register/', register_view, name='register'),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from system.views import (
    admin_car_list, admin_msg, order_list,
    car_created, order_update, order_delete, msg_delete
)
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_car_list, name='adminIndex'),  # root URL
    path('listOrder/', order_list, name="order_list"),
    path('<int:id>/editOrder/', order_update, name="order_edit"),
    path('<int:id>/deleteOrder/', order_delete, name="order_delete"),
    path('create/', car_created, name="car_create"),
    path('message/', admin_msg, name='message'),
    path('<int:id>/deletemsg/', msg_delete, name="msg_delete"),
    path('car/', include('system.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

# Static and media files for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




