from django.db import models



class Child(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1)
    pin = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return "{} {}, {}".format(self.first_name, self.last_name, self.middle_initial)


CHILD_STATUS = [
    ("in", "checked_in"),
    ("out", "checked_out"),
]

class Report(models.Model):
    child = models.ForeignKey(Child)
    time_created = models.DateTimeField(auto_now_add=True)
    child_status = models.CharField(max_length=3, choices=CHILD_STATUS)
