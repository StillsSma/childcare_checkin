from django.db import models



class Child(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1)
    pin = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return "{} {}, {}".format(self.first_name, self.last_name, self.middle_initial)


    def checked_in(self):
        return Report.objects.filter(child=self.id, child_status="in").last()
    def checked_out(self):
        return Report.objects.filter(child=self.id, child_status="out").last()

CHILD_STATUS = [
    ("in", "CHECK IN"),
    ("out", "CHECK OUT"),
]

class Report(models.Model):
    child = models.ForeignKey(Child)
    time_created = models.DateTimeField(auto_now_add=True)
    child_status = models.CharField(max_length=3, choices=CHILD_STATUS)

    
