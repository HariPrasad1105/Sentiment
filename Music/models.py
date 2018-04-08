from django.db import models


class LoginDetails(models.Model):
    email_id = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=20, null=False)
    user_name = models.CharField(max_length=50)

    def __str__(self):
    	return self.email_id + self.password + self.user_name


class sentiment(models.Model):
	tweet = models.IntegerField()
	sentiment = models.CharField(max_length=140)
