from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.


def student_details(request, pk):
    stu = Student.objects.get(id=pk)  # stu is student ovject
    serializer = StudentSerializers(stu)  # serializer is  Student SErializer
    #json_data = JSONRenderer().render(serializer.data)  # serializer.data is python data
    # json_data =json data
    #return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data)


# Query Set - All student Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    return JsonResponse(serializer.data,safe=False)

