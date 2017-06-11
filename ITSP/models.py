from django.db import models
from multiselectfield import MultiSelectField
clubs 			= 	(('Aeromodelling Club','Aeromodelling Club'),('Biotech Club','Biotech Club'),('Electronics And Robotics Club','Electronics And Robotics Club'),('Web and Coding Club','Web and Coding Club'))
optionsForBill 	= 	(('yes',"Yes"),('no',"No"),)
slotChoices		= 	(('one','One'),('two','Two'))
class passwordList(models.Model):
    password = models.CharField(max_length=100)
class team(models.Model):
    team_name		=	models.CharField(max_length=100)
    team_id 		= 	models.IntegerField()
    password 		= 	models.CharField(max_length=100)
    project_name	= 	models.CharField(max_length=100)
    description		=	models.TextField(default=None)
    member1			=	models.CharField(max_length=100)
    member2 		= 	models.CharField(max_length=100,blank=True)
    member3 		= 	models.CharField(max_length=100,blank=True)
    member4 		= 	models.CharField(max_length=100,blank=True)
    mentor			=	models.CharField(max_length=100)
    club 			=	MultiSelectField(choices=clubs)
    slot 			= 	models.CharField(choices=slotChoices,max_length=5)
    teamPic 		= 	models.ImageField(upload_to = 'images/',blank=True,null=True)
    documentation 	= 	models.FileField(upload_to="documents/")
    video 			= 	models.URLField(max_length=400,blank=True,null=True)
    bill 			= 	models.CharField(choices=optionsForBill,max_length=100)
