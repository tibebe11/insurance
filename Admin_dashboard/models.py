from django.db import models



class InsuranceCompany(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='insurance_images')
    description = models.TextField()
    insurable_cars = models.IntegerField()
    non_insurable_cars = models.IntegerField()

    def __str__(self):
        return self.name