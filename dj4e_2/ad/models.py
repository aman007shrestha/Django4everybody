from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
# Create your models here.
class Ad(models.Model):
	title = models.CharField(max_length=200,
		validators = [MinLengthValidator(2, "Please Enter atlease 2 character")]
		)
	price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	# picture field as Binary Field
	picture = models.BinaryField(editable=True, null=True, blank=True)
	content_type = models.CharField(max_length=256, null=True, blank=True,
		help_text="The MIMEtype of file")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title