from rest_framework import serializers
from vietintelsocial_user_app.vietintelsocial_http.models.user import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    userID = serializers.IntegerField(source='id')
    userRole = serializers.CharField(source='role')
    userEmail = serializers.CharField(source='email')
    userPassword = serializers.CharField(source='password')
    userAvatar = serializers.CharField(source='avatar')
    userName = serializers.CharField(source='name')
    userDisplayName = serializers.CharField(source='display_name')
    userCity = serializers.CharField(source='city')
    userGender = serializers.CharField(source='gender')
    userStatus = serializers.CharField(source='status')
    userNotification = serializers.CharField(source='get_notification')
    userAnswerNumbers = serializers.IntegerField(source='answer_count')
    userQuestionNumbers = serializers.IntegerField(source='question_count')
    userPoint = serializers.IntegerField(source='point')

    class Meta:
        model = User
        fields = '__all__'
