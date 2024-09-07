from django.contrib import admin
from app.models import Qualification, Specialization, Gender, Doctor, patient
# Register your models here.


admin.site.register(Qualification)
admin.site.register(Specialization)
admin.site.register(Gender)
admin.site.register(Doctor)
admin.site.register(patient)