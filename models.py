from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField(default=1234)

class Contact_Us(models.Model):
    message = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)


class Add_product(models.Model):
    product_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500)
    pic  = models.ImageField(upload_to='img')


class leave_reply(models.Model):
    comment = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=100)





class branding(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class prize(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name





class product(models.Model):
    branding_id = models.ForeignKey(branding,on_delete=models.CASCADE,blank=True,null=True)
    prize_id = models.ForeignKey(prize,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    img=models.ImageField(upload_to="image")

    def __str__(self) -> str:
        return self.name
    


class add_cart(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE,blank=True,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    img=models.ImageField(upload_to="image")
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()
    total=models.IntegerField()

    def __str__(self) -> str:
        return self.name


    
