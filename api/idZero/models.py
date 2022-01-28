from django.db import models

# Create your models here.
class Provider(models.Model):
    # store provider types and use for analytics 
    pass

class QueryManager(models.Manager):
    # store logs here, how many connected to api, analytics for route history 
    pass

