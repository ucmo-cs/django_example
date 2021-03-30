from django.urls import path
from planner import views

urlpatterns = [
    # Return all courses
    path('courses', views.courses_list),
    # Return all semesters
    path('semesters', views.semesters_list),
    # Return all course/semester pairs
    path('offered_in', views.offered_in_list),
    # Return semester titles that a course is offered in
    path('courses/offered_in/<slug:cid>', views.offered_in_course),
]
