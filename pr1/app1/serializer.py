from rest_framework import serializers
from app1.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Get Out Motherfucker!!')
        return value