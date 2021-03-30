from rest_framework import serializers
from planner.models import Courses,Semesters,Offered_In

class CoursesSerializer(serializers.ModelSerializer):
    # This serializes a list of Course objects, with all fields
    class Meta:
        model = Courses
        fields = ['course_id', 'description']

class SemestersSerializer(serializers.ModelSerializer):
    # This serializes a list of Semester objects, with all fields
    class Meta:
        model = Semesters
        fields = ['semester_id', 'title']

class SemestersTitleSerializer(serializers.ModelSerializer):
    # This serializes a list of Semester objects, with only the
    # title field.
    class Meta:
        model = Semesters
        fields = ['title']

class Offered_InSerializer(serializers.ModelSerializer):
    # This serializes a list of Offered_In objects, and uses
    # the Serializers for Course and Semester to serialize the 
    # Foreign Key fiels for them.
    course = CoursesSerializer(read_only=True)
    semester = SemestersSerializer(read_only=True)
    class Meta:
        model = Offered_In
        fields = ['course','semester']

class Offered_InTitlesSerializer(serializers.ModelSerializer):
    # This serializes a list of Offered_In objects, and uses
    # the Serializer for Semester to just serialize the 
    # Titles
    semester = SemestersTitleSerializer(read_only=True)
    class Meta:
        model = Offered_In
        fields = ['semester']
