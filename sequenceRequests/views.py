from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Request
from .serializers import RequestSerializer

class RequestList(APIView):
	def get(self, request, format=None):
		previous_requests = Request.objects.all()
		serializer = RequestSerializer(previous_requests, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = RequestSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRequestList(APIView):
	def get(self, request, user, format=None):
		user_requests = Request.objects.filter(user=user)
		serializer = RequestSerializer(user_requests, many=True)
		return Response(serializer.data)

class RequestDetail(APIView):
	def get_object(self, pk):
		try:
			return Request.objects.get(pk=pk)
		except Request.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		previous_request = self.get_object(pk)
		serializer = RequestSerializer(previous_request)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		previous_request = self.get_object(pk)
		serializer = RequestSerializer(previous_request, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		previous_request = self.get_object(pk)
		previous_request.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

