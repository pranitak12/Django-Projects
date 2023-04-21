from django.db import models

# Create your models here.

class service(models.Model):
    service_title = models.CharField(max_length=100)
    service_desc = models.TextField()

class service_booking(models.Model):
    location = (('M','Mumbai'),
                ('P','Pune'),
                ('N','Navi Mumbai'),
                ('G','Goa'))
    
    service = (('AC','Auto Clean'),
               ('AR','Auto Repair'),
               ('CI','Car Inspection'))

    payment =  (('PP','PayPal'),
               ('C','Cash'),
               ('N','NetBanking'))
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    pickup_loc = models.CharField(max_length=1,choices=location)
    drop_loc = models.CharField(max_length=1,choices=location)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    service = models.CharField(max_length=2,choices=service)
    request = models.TextField()
    payment = models.CharField(max_length=2,choices=payment)

class team(models.Model):
    picture = models.ImageField(upload_to='Media/')
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)

class reviews(models.Model):
    picture = models.ImageField(upload_to='Media/')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    review = models.TextField()

class car(models.Model):
    picture = models.ImageField(upload_to='Media/')
    name = models.CharField(max_length=100)
    purchase_year = models.IntegerField()
    car_type = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price = models.IntegerField()

class car_details(models.Model):
    car_picture = models.ImageField(upload_to='Media/')
    car_name = models.CharField(max_length=100)
    car_desc = models.TextField()
    purchase_year = models.IntegerField()
    car_type = models.CharField(max_length=50)
    mileage = models.IntegerField()
    features = models.CharField(max_length=100)
  
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
  
    def register(self):
        self.save()
  
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
  
        return False