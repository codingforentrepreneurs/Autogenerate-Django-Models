from django.db import models


class Topic(models.Model):
    # index = models.BigIntegerField(blank=True, null=True)
    tag = models.CharField(max_length=120, blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    percent = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    percent_human = models.CharField(max_length=120, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'topics'