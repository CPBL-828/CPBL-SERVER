from rest_framework import serializers
from . import models


class LectureRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LectureRoom
        fields = \
            '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lecture
        fields = \
            '__all__'


class LectureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LectureStatus
        fields = \
            '__all__'


class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assign
        fields = \
            '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = \
            '__all__'


class TestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestStatus
        fields = \
            '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Record
        fields = \
            '__all__'


class PlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Planner
        fields = \
            '__all__'
