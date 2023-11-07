from django.db import models

# Create your models here.

class details(models.Model):
    date_time = models.CharField(max_length=30)
    roll_number=models.CharField(max_length=255)
    mobile_model=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=13)
    complaint=models.TextField()
    condition = models.CharField(max_length=255)
    remark_status = models.CharField(max_length=100)
    technition = models.CharField(max_length=100)
    def __str__(self):
        return self.customer_name
    
class staff(models.Model):
    emp_code = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    mobile_number=models.CharField(max_length=100)
    email = models.EmailField()
    emp_name=models.CharField(max_length=100)
    address=models.TextField()