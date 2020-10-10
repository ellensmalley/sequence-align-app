from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	user = serializers.CharField(max_length=100)
	sequence = serializers.CharField(max_length=300)
	status = serializers.CharField(max_length=100, required=False, allow_blank=True, default="RUNNING")
	protein = serializers.CharField(max_length=100, required=False, allow_blank=True)
	location = serializers.CharField(max_length=300, required=False, allow_blank=True)

	def create(self, validated_data):
		return Request.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.user = validated_data.get('user', instance.user)
		instance.sequence = validated_data.get('sequence', instance.sequence)
		instance.status = validated_data.get('status', instance.status)
		instance.protein = validated_data.get('protein', instance.protein)
		instance.location = validated_data.get('location', instance.location)
		instance.save()
		return instance

	def update_with_result(self, instance, found_protein, found_location):
		instance.status = "DONE"
		instance.protein = found_protein
		instance.location = found_location
		instance.save()
		return instance
