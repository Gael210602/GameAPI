# serializers.py
from rest_framework import serializers
import bcrypt

from .models import Attempt, GameVariables, Level, Session, SessionData, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'password','user_type', 'name','user_name','email', 'dob', 'country')
    def create(self, validated_data):

        bytePwd = validated_data['password'].encode("utf-8")
        mySalt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytePwd, mySalt)

        user = User(
            name=validated_data['name'],
            user_type = "User",
            user_name=validated_data['user_name'],
            password = hash.decode('utf-8'),
            email=validated_data['email'],
            dob=validated_data['dob'],
            country=validated_data['country'],
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        h = hashlib.new('sha256')
        h.update(str(validated_data['password']).encode('utf-8'))
        
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.password =  h.hexdigest()
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('session_id', 'sign_in', 'sign_out','user_id', 'jwt')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('level_id', 'song_name', 'difficulty', 'duration')

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ('attempt_id', 'level_id', 'status', 'user_id', 'score')


class VariablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameVariables
        fields = ('variables_id', 'user_id', 'lvl', 'video', 'Hs1', 'Hs2', 'Hs3', 'FirstTime', 'score')


class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = ('session_data_id', 'user_id', 'time')
