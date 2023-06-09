from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class GenericCreateAPI(APIView):
    serializer_class = None

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GenericListAPI(APIView):
    serializer_class = None
    query_set = None
    model = None

    def _get_query_set(self, pk=None):
        if not self.query_set and not self.model:
            raise AttributeError("query_set and model are missing")
        if pk is not None:
            return self.model.objects.get(id=pk)
        if not self.query_set:
            return self.model.objects.all()
        return self.query_set

    def get(self, request, pk=None):
        def _get_serializer(_pk=None):
            if _pk is not None:
                return self.serializer_class(self._get_query_set(_pk))
            return self.serializer_class(self._get_query_set(), many=True)
        return Response(_get_serializer(pk).data)


class GetObject:
    serializer_class = None
    model = None
    look_up_field = "pk"

    def _get_object(self, look_up_field=None):
        payload = {self.look_up_field: look_up_field}
        return get_object_or_404(self.model, **payload)


class GenericUpdateAPI(GetObject, APIView):

    def put(self, request, pk=None):
        obj = self._get_object(look_up_field=pk)
        serializer = self.serializer_class(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GenericDeleteAPI(GetObject, APIView):

    def delete(self, request, pk=None):
        obj = self._get_object(look_up_field=pk)
        obj.delete()
        return Response({"message": "deleted"})


class GenericUpdateOrDeleteAPI(GenericUpdateAPI, GenericDeleteAPI):
    pass


class GenericCreateOrListAPI(GenericCreateAPI, GenericListAPI):
    pass
