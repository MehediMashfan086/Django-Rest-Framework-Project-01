from django.shortcuts import render

from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Model Object - Single Student Data

def student_detail(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type = 'application/json')