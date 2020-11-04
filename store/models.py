from django.db import models

###########################Models###################################


class Category(models.Model):
    name= models.CharField(max_length=20)    

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

##################################################################################

##################################################################################

class Product(models.Model):
    name= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    description= models.TextField(default='',null=True,blank=True)
    image= models.ImageField(upload_to='product_img/')
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id: 
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

##################################################################################

##################################################################################

class Customer(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=25)
    phone= models.IntegerField()
    password=models.CharField(max_length=50)
    confirmation=models.CharField(max_length=50 ,default="" ,null=True ,blank=True)

    

##################################################################################

##################################################################################


    

    




