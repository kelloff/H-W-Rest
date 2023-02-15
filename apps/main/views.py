#Django
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User

#DRF
from rest_framework.views import APIView
from rest_framework.response import Response

#Local
from .models import Car


class CarView(APIView):
    """Car View"""


    def get(
        self,
        request: WSGIRequest,
        *args,
        **kwargs
    ) -> Response:
        cars = Car.objects.all()
        result: list[dict[str,str]] = []

        car: Car
        for car in cars:
            result.append({
                "bra": car.brand,
                "model": car.model,
                "price": car.price,
                'owner':car.owner.username
            })
            
        return Response(
            {
                "cars":result
            },
            status=200
        )