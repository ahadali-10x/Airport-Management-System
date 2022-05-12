from django.contrib import admin

# Register your models here.
from .models import *
	# Register your models here.

admin.site.register(Airplane)
admin.site.register(Coorporation) 
admin.site.register(Flies)
admin.site.register(Employee)
admin.site.register(Pilot)
admin.site.register(Hangar)
admin.site.register(Owner) 
admin.site.register(Owns)
admin.site.register(Person)
admin.site.register(PlaneType)
admin.site.register(Service)
admin.site.register(WorksOn)