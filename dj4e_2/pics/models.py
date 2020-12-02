from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
from django.conf import settings


class Ad(models.Model):
	title = models.CharField(max_length=100,
		validators=[MinLengthValidator(3, "Must be greater or equal to 3 character")]
		)
	price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	text=models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	# picture field
	#  BinaryField is a special field to store raw binary data. It can be assigned bytes
	#  , bytearray, or memoryview.
	picture = models.BinaryField(null=True, blank=True, editable=True)
	content_type = models.CharField(max_length=256, null=True, blank=True, 
                                    help_text='The MIMEType of the file')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




	def __str__(self):
		return self.title