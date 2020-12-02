from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
# Create your models here.
class Forum(models.Model):
	title = models.CharField(max_length=100,
		validators=[MinLengthValidator(2, "Please enter atleast 2 character")],
		help_text='title for the forum'
		)
	text=models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Like',
		related_name='likes_forum')
	comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment',
		related_name='forum_comments')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	text = models.TextField(
		validators=[MinLengthValidator(2, "Atleast 2 character comments")]
		)
	forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		if len(self.text) < 15:
			return self.text
		return self.text[:12] + ' ..' 


class Like(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('owner', 'forum')

	def __str__(self) :
		return '%s likes %s'%(self.owner.username, self.forum.title[:10])

	