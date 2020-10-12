from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	user = serializers.CharField(max_length=100)
	sequence = serializers.CharField(max_length=300)
	status = serializers.CharField(max_length=100, required=False, allow_blank=True, default="RUNNING")
	genome = serializers.CharField(max_length=100, required=False, allow_blank=True)
	location = serializers.CharField(max_length=100, required=False, allow_blank=True)
	protein = serializers.CharField(max_length=100, required=False, allow_blank=True)

	def create(self, validated_data):
		return Request.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.user = validated_data.get('user', instance.user)
		instance.sequence = validated_data.get('sequence', instance.sequence)
		instance.status = validated_data.get('status', instance.status)
		instance.genome = validated_data.get('genome', instance.genome)
		instance.location = validated_data.get('location', instance.location)
		instance.protein = validated_data.get('protein', instance.protein)
		instance.save()
		return instance

	def update_with_result(self, found_genome, found_location, found_protein):
		self.instance.status = "DONE"
		self.instance.genome = found_genome
		self.instance.location = found_location
		self.instance.protein = found_protein
		self.instance.save()
		return self.instance
