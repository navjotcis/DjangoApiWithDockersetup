from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employees
from . serializers import EmployeesSerializers


class EmployeeList(APIView):

	def get(self, request, *args, **kwargs):
		"this is for reading to getting data"
		employees1 = Employees.objects.all()
		serializer = EmployeesSerializers(employees1, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		"this is for submitting data"
		data = request.data
		serializer = EmployeesSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.data, status=400)


class EmployeeDetailView(APIView):

	def get_object(self, id=None):
		try:
			return Employees.objects.get(pk=id)
		except Employees.DoesNotExist as e:
			return Response({"error": "Employees matching query does not exist"}, status=404)

	def get(self, request, id=None):
		instance = self.get_object(id)
		serializer = EmployeesSerializers(instance)
		return Response(serializer.data)

	def put(self, request, id=None):
		data = request.data
		instance = self.get_object(id)
		serializer = EmployeesSerializers(instance, data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		return Response(serializer.data, status=400)

	def delete(self, request, id=None):
		instance = self.get_object(id)
		instance.delete()
		return HttpResponse(status=204)
