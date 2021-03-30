from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from planner.models import Courses, Semesters, Offered_In
from planner.serializers import CoursesSerializer, SemestersSerializer, Offered_InSerializer, Offered_InTitlesSerializer

# Create your views here.

@csrf_exempt
def courses_list(request):
    """
    List all courses.
    """
    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def semesters_list(request):
    """
    List all semesters.
    """
    if request.method == 'GET':
        semesters = Semesters.objects.all()
        serializer = SemestersSerializer(semesters, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def offered_in_list(request):
    """
    List all pairs of course and semester offered
    """
    if request.method == 'GET':
        offered_ins = Offered_In.objects.all()

        serializer = Offered_InSerializer(offered_ins, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def offered_in_course(request, cid):
    """
    List the semesters a course is offered in.
    """
    if request.method == 'GET':
        # Note the double underscore in the filter query parameter
        # says you want to look at the course_id sub-field of the
        # course field.
        offered_ins = Offered_In.objects.filter(course__course_id=cid)

        serializer = Offered_InTitlesSerializer(offered_ins, many=True)
        return JsonResponse(serializer.data, safe=False)
