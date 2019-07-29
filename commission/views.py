from rest_framework.viewsets import ModelViewSet

from .serializer import CommissionSerializer
from .models import Commission

class CommissionViewSet(ModelViewSet):
	queryset = Commission.objects.all()
	serializer_class = CommissionSerializer
