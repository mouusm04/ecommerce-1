from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey 

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    # slug = models.SlugField(max_length = 250, null = True, blank = True)
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.90)
    image       = models.ImageField(upload_to='home/', null=True, blank=True)
    SubCatagory = models.ForeignKey('SubCatagory', blank=True, null=True, on_delete=models.CASCADE)
    Catagory = models.ForeignKey('Catagory', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __str__(self):
        return str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url     

    # def get_absolute_url(self):
    #         return reverse('product', kwargs={'slug': self.slug}) 

class SubCatagory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/', null=True, blank=True)
    catagory = models.ForeignKey('Catagory', blank=True, null=True, on_delete=models.CASCADE)

    # slug = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
            return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url         
      

class Catagory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/', null=True, blank=True)
    # slug = models.SlugField(max_length = 250, null = True, blank = True)


    def __str__(self):
            return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url        

    # def get_absolute_url(self):
    #     return reverse('Catagory', kwargs={'slug': self.slug})         





# class Catagory(MPTTModel):
#     name = models.CharField(max_length=200)
#     parent = TreeForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    


#     def __str__(self):                           
#         full_path = [self.name]            
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent

#         return ' -> '.join(full_path[::-1])
