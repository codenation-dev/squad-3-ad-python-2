from django.contrib import admin
from commission.models import Commission, Plan

admin.site.register([Commission, Plan])
