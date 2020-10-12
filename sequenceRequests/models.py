from django.db import models

# Proteins to be searched over
# class Protein(models.Model):
#     name = models.CharField(max_length=100)
#     searcheable = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# Request made by user to search within protein list for sequence
class Request(models.Model):
    user = models.CharField(max_length=100)
    sequence = models.CharField(max_length=300)
    status = models.CharField(max_length=100)
    genome = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    protein = models.CharField(max_length=100, blank=True)

# Result of one request (many to one relationship - may extend app to return many proteins)
# class Result(models.Model):
#     request = models.ForeignKey(Request, on_delete=models.CASCADE)
#     protein = models.ForeignKey(Protein, on_delete=models.PROTECT)
#     location = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

