from django.db import models
from django.contrib.auth.models import User


class HouseDetails(models.Model):

    VIEWSS_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    CONDITION_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    GRADE_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    WATERFRONT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )


    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    sqft_living = models.IntegerField()
    sqft_lot = models.IntegerField()
    floors = models.IntegerField()
    sqft_above = models.IntegerField()
    sqft_basement = models.IntegerField()
    zipcode = models.IntegerField()
    sqft_living15 = models.IntegerField()
    sqft_lot15 = models.IntegerField()
    waterfront = models.CharField(max_length=50, choices=WATERFRONT_CHOICES)
    year_renovated = models.IntegerField()
    year_built = models.IntegerField()
    viewss = models.CharField(max_length=50, choices=VIEWSS_CHOICES)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES)
    price = models.FloatField()

