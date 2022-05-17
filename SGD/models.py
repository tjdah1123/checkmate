from django.db import models

class Professor(models.Model):
    id = models.CharField(primary_key=True, max_length=123)
    pw = models.CharField(max_length=123)
    email = models.CharField(max_length=123)
    name = models.CharField(max_length=123)
    lecture = models.CharField(max_length=123)

    def __str__(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'professor'


class CheckStudent(models.Model):
    count = models.AutoField(primary_key=True)
    check_id = models.CharField(max_length=1123)
    check_name = models.CharField(max_length=1123)
    check_major = models.CharField(max_length=1123)
    check_lecture = models.CharField(max_length=1123)
    check_image = models.CharField(max_length=1123)
    check_in_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'check_student'