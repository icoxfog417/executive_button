from django.db import models


class Remuneration(models.Model):

    edinet_code = models.CharField(max_length=6)
    sec_code = models.CharField(max_length=5)
    filer_name = models.TextField()
    doc_description = models.TextField()
    doc_id = models.CharField(max_length=8)
    period_start = models.CharField(max_length=10)
    period_end = models.CharField(max_length=10)
    amount = models.IntegerField()
    number = models.IntegerField()
