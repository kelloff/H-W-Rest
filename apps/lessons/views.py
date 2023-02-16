# Django
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
#DRF
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

#Local
from lessons.models import Comics
from auths.models import CustomUser



class ComicsView(APIView):
    """Comics view."""

    def get(
        self,
        request: WSGIRequest,
        *args,
        **kwargs
    ) -> Response:
        comicses: QuerySet[Comics] = Comics.objects.all() 
        result: list[dict[str,str]] = []

        comics: Comics
        for comics in comicses:
            print(comics.image)
            result.append({
                "title": comics.title,
                "image": str(comics.image.url),
                "price": comics.price
            })

        return Response({
            'result': result
        }, status=200)


class CustomUserView(APIView):
    """User view."""

    def get(
        self,
        request: WSGIRequest,
        *args,
        **kwargs
    ) -> Response:
        users: QuerySet[CustomUser] = CustomUser.objects.all()
        users_info: list[dict[str,str]] = []

        user: CustomUser
        for user in users:
            users_info.append({
                'username': user.username,
                'email': user.email,
                'password': user.password,
                'is_superuser': user.is_superuser,
                'date joined': user.date_joined,
            })

        return Response({
            'users_info': users_info
        }, status=200)