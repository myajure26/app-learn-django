from django.shortcuts import render

# Create your views here.
def course_list(request):
    return render(request, 'courses/courses.html')

def course_details(request):
    pass

def course_lessons(request):
    pass