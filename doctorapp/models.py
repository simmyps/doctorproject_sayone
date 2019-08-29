from django.db import models

class TbAddpatient(models.Model):
	pname=models.CharField(max_length=50)  #patient name
	paddress=models.CharField(max_length=50) #patient address
	pcondition=models.CharField(max_length=50) #patient medical condition
	pmedicine=models.CharField(max_length=50) #patient medicine
	dname=models.CharField(max_length=50) #doctor name

class meta:
	db_table="TbAddpatient"
