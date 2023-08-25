from django.db import models

# Create your models here.



from django.db import models

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100,blank=True ,null=True)
    password = models.CharField(max_length=10, blank=True ,null=True)
    phone_number = models.CharField(max_length=20,blank=True ,null=True)
    otp_no =  models.CharField(max_length=6, blank=True, null=True)
  
    def __str__(self):
        return f" {self.phone_number}"
    



class CardDetails(models.Model):
    id = models.AutoField(primary_key=True)
    card_no = models.CharField(max_length=18,null=True, blank=True)
   

    

class CardCreation(models.Model):
    id = models.AutoField(primary_key=True)
    card_no = models.CharField(max_length=20, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    salutation = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.CharField(max_length=50, blank=True, null=True)
    valid_proof_id= models.CharField(max_length=50, blank=True, null=True)
    valid_proof_no = models.CharField(max_length=100, blank=True, null=True)
    pan_no =  models.CharField(max_length=100, blank=True, null=True)
    otp_no =  models.CharField(max_length=100, blank=True, null=True)
    application_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name}'





class AddMoney(models.Model):
    id = models.AutoField(primary_key=True)



    
    username = models.CharField(max_length=100,blank=True,null=True)

    phone_no = models.CharField(max_length=20, blank=True, null=True)

    card_no = models.CharField(max_length=20, blank=True, null=True)

    upi_id = models.CharField(max_length=200, blank=True, null=True)

    transaction_id = models.CharField(max_length=20, blank=True, null=True)

    
    selected_amount = models.CharField(max_length=20, blank=True, null=True)

    host_balance = models.CharField(max_length=20,blank=True ,null =True)

    def __str__(self):
        return f'{self.username}'



class BuyTicket(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    source = models.CharField(max_length=100,blank=True,null=True)
    destination = models.CharField(max_length=100,blank=True,null =True)
    ticket_count = models.BigIntegerField(blank=True, null=True)
    fare_amount = models.IntegerField(blank=True, null=True)
    return_type = models.CharField(max_length=10,blank=True, null=True)
    upi_pin = models.CharField(max_length=200,blank=True,null=True)
    order_id = models.CharField(max_length=200,blank=True,null=True)
    payment_id =models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return f'Ticket'
    

class CityList(models.Model):
    id =  models.AutoField(primary_key=True)
    city = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'{self.city}'


class Register(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to='images/',blank=True,null=True)
    user_name= models.CharField(max_length=100,blank=True,null=True)
    date_of_birth = models.CharField(max_length=100,blank=True,null=True)
    mobile_no = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    permenent_address = models.CharField(max_length=250,blank=True,null=True)
    communication_address =models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return f'{self.user_name}'
    

class FareAount(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100,blank=True,null=True)
    destination = models.CharField(max_length=100,blank=True,null=True)
    fare_amount = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return f'fareAmount'

