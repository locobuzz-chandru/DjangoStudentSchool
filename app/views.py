from rest_framework.response import Response
from .models import Student, School
from rest_framework.views import APIView
from app.serializers import SchoolSerializer, StudentSerializer


class GenericCreateAPI:
    def create(self, request, serializer_class):
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SchoolAPI(GenericCreateAPI, APIView):
    def post(self, request):
        return super().create(request, SchoolSerializer)

    def get(self, request):
        school_list = School.objects.all()
        serializer = SchoolSerializer(school_list, many=True)
        return Response(serializer.data)

    def put(self, request):
        school_obj = School.objects.get(id=request.data.get("id"))
        serializer = SchoolSerializer(school_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        school_obj = School.objects.get(id=request.data.get("id"))
        serializer = SchoolSerializer(data=request.data)
        school_obj.delete()
        return Response(serializer.data)


class StudentAPI(GenericCreateAPI, APIView):
    def post(self, request):
        return super().create(request, StudentSerializer)

    def get(self, request):
        school_list = Student.objects.all()
        serializer = StudentSerializer(school_list, many=True)
        return Response(serializer.data)

    def put(self, request):
        school_obj = Student.objects.get(id=request.data.get("id"))
        serializer = StudentSerializer(school_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        school_obj = Student.objects.get(id=request.data.get("id"))
        serializer = StudentSerializer(data=request.data)
        school_obj.delete()
        return Response(serializer.data)
