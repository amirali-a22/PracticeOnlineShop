from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not full_name:
            raise ValueError('Users must have a fullname')

        user = self.model(email=self.normalize_email(email), full_name=full_name, password=password)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email=email, full_name=full_name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
