from django.db import models


# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     # sets created_at only once when the record is created
#     updated_at = models.DateTimeField(auto_now=True)
#     # updates updated_at every time the record is saved
#     class Meta:
#         abstract = True  # ✅ This tells Django NOT to create a table for it
    
    
# Create your models here.
class Card(models.Model):
    # id is the default field created by django therefore no need to create it
    title = models.CharField(max_length=30)
    text_body = models.TextField(max_length=400)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.TextField(blank=True,help_text="Comma-separated tags (e.g., productivity, habits, reflection)")
    # blank=True is enough to make it optional in forms.
    source = models.TextField(blank=True, help_text="Can be a URL (https://...) or plain text reference")
    image = models.ImageField(upload_to='card_images/', null=True, blank=True)
    is_favourite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # sets created_at only once when the record is created
    updated_at = models.DateTimeField(auto_now=True)
    # updates updated_at every time the record is saved
    
    def __str__(self):
        return self.title 
    
    # class Meta:
    #     db_table = 'card_details'
    # To override the database table name, use the db_table parameter in class Meta.
    

class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    # sets created_at only once when the record is created
    updated_at = models.DateTimeField(auto_now=True)
    # updates updated_at every time the record is saved
    
    def __str__(self):
        return self.name
    
    

    
    