from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVarity(models.Model):
    # for the dropdown menu selection of chai varities, we define enums
    CHAI_TYPES = [
        ('MASALA', 'Masala Chai'),
        ('GINGER', 'Ginger Chai'),
        ('CARDAMOM', 'Cardamom Chai'),
        ('SUGAR', 'Sugar Chai'),
        ('MILK', 'Milk Chai'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2 , default=0.00)
    image = models.ImageField(upload_to='chais/') # for the image store we need to make changes in settings.py later (MEDIA_URL and MEDIA_ROOT) & aslo in main urls.py import settings and static
    created_at = models.DateTimeField(default= timezone.now)
    chai_type = models.CharField(max_length=10, choices=CHAI_TYPES)
    
    # for better representation of the model object in admin panel and shell
    def __str__(self):
        return self.name 

# One To Many Relationship : One ChaiVarity can have multiple Reviews

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews') # when we delete a chai varity all its reviews will be deleted too because of on_delete=models.CASCADE
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField() # we can add validators later to restrict rating between 1-5
    comment = models.TextField()
    review_added = models.DateTimeField(default= timezone.now)
    
    # for better representation of the model object in admin panel and shell
    def __str__(self):
        return f'Review for {self.chai.name} by {self.user.username}'
    
# Many To Many Relationship : One Store have multiple ChaiVarities and one ChaiVarity can be avlable on multiple Stores

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')
    
    # for better representation of the model object in admin panel and shell
    def __str__(self):
        return self.name


# One To One Relationship : One ChaiVarity have one ChaiCertification

class ChaiCertification(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certification')
    certification_name = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default= timezone.now)
    expiry_date = models.DateTimeField()
    
        
    # for better representation of the model object in admin panel and shell
    def __str__(self):
        return f'Certification for {self.chai.name}: {self.certification_name}'

    
    