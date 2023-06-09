from .models import Student, School
from app.serializers import SchoolSerializer, StudentSerializer
from utils.generics import GenericCreateOrListAPI, GenericUpdateOrDeleteAPI


class SchoolAPI(GenericCreateOrListAPI, GenericUpdateOrDeleteAPI):
    serializer_class = SchoolSerializer
    model = School

    def put(self, request, pk=None):
        _pk = request.data.pop("id")
        return super().put(request, _pk)

    def delete(self, request, pk=None):
        _pk = request.data.pop("id")
        return super().delete(request, _pk)


class StudentAPI(GenericCreateOrListAPI, GenericUpdateOrDeleteAPI):
    serializer_class = StudentSerializer
    model = Student

    def put(self, request, pk=None):
        _pk = request.data.pop("id")
        return super().put(request, _pk)

    def delete(self, request, pk=None):
        _pk = request.data.pop("id")
        return super().delete(request, _pk)
