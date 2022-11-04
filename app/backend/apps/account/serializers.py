from backend.apps.utils.serializers import CustomSerializer

from .models import MyUser


class MyUserSerializer(CustomSerializer):
    class Meta:
        model = MyUser
        exclude = []
