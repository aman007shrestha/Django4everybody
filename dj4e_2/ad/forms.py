from django import forms
from .models import Ad
from django.core.files.uploadedfile import InMemoryUploadedFile
from .humanize import natural_size


class CreateForm(forms.ModelForm):
	max_upload_limit = 2 * 1024 * 1024
	max_upload_limit_text = natural_size(max_upload_limit)
	#  picture is here in memory onject 'picture' is corresponding feild name
	# to be used for form
	picture = forms.FileField(required=False, label='File to upload < ' + max_upload_limit_text)
	upload_field_name = 'picture'


	class Meta:
		model = Ad
		fields = ['title', 'price', 'text', 'picture']


	def clean(self):
		cleaned_data = super().clean()
		pic = cleaned_data.get('picture')
		if pic is None:
			return 
		if len(pic) > self.max_upload_limit:
			self.add_error('picture', 'File must be < ' + self.max_upload_limit_text + ' bytes')

	# convert uploaded file into picture
	def save(self, commit=True):
		print('hi')
		instance = super(CreateForm, self).save(commit=False)
		pic = instance.picture
		if isinstance(pic, InMemoryUploadedFile):
			bytearr = pic.read()
			instance.content_type = pic.content_type
			instance.picture = bytearr
			print('4')

		if commit:
			print('comiting')
			instance.save()
		print('5')
		return instance

