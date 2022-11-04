from backend.apps.utils.serializers import EmptySerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import MyUser
from .serializers import MyUserSerializer


class MyUserViewSet(viewsets.GenericViewSet):
    model = MyUser
    queryset = model.objects.all()
    serializer_class = MyUserSerializer

    @action(methods=["POST"], detail=False, serializer_class=EmptySerializer)
    def test(self, request):
        user_id = request.user.id
        return Response(
            {"status": "Done!", "data": f"Your id is {user_id}"},
            status=status.HTTP_200_OK,
        )
