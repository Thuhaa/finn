from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class FinnUserManager(BaseUserManager):
	def create_user(self, first_name, last_name, email, password):

		if not email:
			raise ValueError("Users must have an email address")

		finnuser = self.model(
			first_name=first_name,
			last_name=last_name,
			email=self.normalize_email(email),
			password=password
			)

		finnuser.save(using=self._db)

		return finnuser

	def create_superuser(self, first_name, last_name, email, password):

		finnuser = self.create_user(
			first_name=first_name,
			last_name=last_name,
			email=email,
			password=password
			)

		finnuser.is_admin = True

		finnuser.save(using=self._db)
		
		return finnuser

class FinnUser(AbstractBaseUser):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length = 255, unique=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	objects = FinnUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	def is_staff(self):
		return self.is_admin


	class Meta:
		verbose_name_plural = "Finn Users"
		