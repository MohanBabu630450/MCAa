from django.db import models
class Member(models.Model):
    fristname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)

    #def __str__(self):
        #return self.firstname+' '+self.lastname
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return self.fristname
    


# Create your models here.
