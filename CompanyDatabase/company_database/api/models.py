from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    familyName = models.CharField(max_length=100, blank=False, default='')
    lastName = models.CharField(max_length=100, blank=True, default='')
    jobs = models.ManyToManyField('Job', related_name='workers', blank=True)
    workGroups = models.ManyToManyField('WorkGroup', related_name='workers', blank=True)
    def __str__(self):
        return self.name + ' ' + self.familyName

class Job(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    def __str__(self):
        return self.name

class WorkGroup(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    parent = models.ManyToManyField('WorkGroup', related_name='subGroups', blank=True)
    def __str__(self):
        return self.name