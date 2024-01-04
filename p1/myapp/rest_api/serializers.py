from rest_framework import serializers

from .models import MyModel, Student


class MySerialiazer(serializers.ModelSerializer):

    class Meta:
        model = MyModel
        fields = ('title', 'description')


class StudentSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('stuid', 'name', 'roll', 'address')