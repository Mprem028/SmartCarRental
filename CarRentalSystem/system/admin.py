# from django.contrib import admin
# from .models import Car, Order, PrivateMsg
# # Register your models here.

# class CarAdmin(admin.ModelAdmin):
#     list_display = ("car_name", "image", "company_name")
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("car_name", "date", "to", "employee_name")

# class PrivateMsgAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "message")

# admin.site.register(Car, CarAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(PrivateMsg, PrivateMsgAdmin)

from django.contrib import admin
from .models import Car, Order, PrivateMsg

class CarAdmin(admin.ModelAdmin):
    list_display = ("car_name", "company_name", "num_of_seats", "cost_par_day", "like")
    search_fields = ("car_name", "company_name")
    list_filter = ("company_name", "num_of_seats")
    ordering = ("-id",)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("car_name", "employee_name", "date", "to", "cell_no")
    search_fields = ("car_name", "employee_name", "cell_no")
    list_filter = ("date",)
    ordering = ("-date",)

class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
    search_fields = ("name", "email")
    ordering = ("-id",)

admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)
