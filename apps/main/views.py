#Django
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet

#DRF
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#Local
from .serializers import CarsSerializer
from .models import Car

class CarViewSet(ViewSet):
    """Car ViewSet."""
    
    queryset = Car.objects.all()
    print('--------'*10)

    def list(
        self,
        request: WSGIRequest,
        *args,
        **kwargs
    ) -> Response:
        cars: QuerySet[Car] = self.queryset.all()
        serializer: CarsSerializer = CarsSerializer(
            cars,
            many=True
        )
        return Response(
            {
                'data':
                {
                    'cars': serializer.data
                }
            }
        )
