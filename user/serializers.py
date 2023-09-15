from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = self.user.email
        return data
