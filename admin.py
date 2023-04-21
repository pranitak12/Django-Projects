from django.contrib import admin
from .models import service,service_booking,car,car_details,team,reviews,Customer

# Register your models here. carrent123

admin.site.register(service)
admin.site.register(service_booking)
admin.site.register(car)
admin.site.register(car_details)
admin.site.register(team)
admin.site.register(reviews)
admin.site.register(Customer)

