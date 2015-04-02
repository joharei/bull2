from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MemberManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Members must have a valid username')

        member = self.model(
            username=username
        )

        member.set_password(password)
        member.save()

        return member

    def create_superuser(self, username, password, **kwargs):
        member = self.create_user(username, password, **kwargs)

        member.is_admin = True
        member.save()

        return member


class Member(AbstractBaseUser):
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'medlem'
        verbose_name_plural = 'medlemmer'

    username = models.CharField(max_length=50, unique=True, verbose_name='brukernavn')

    first_name = models.CharField(max_length=50, blank=True, verbose_name='fornavn')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='etternavn')

    email = models.EmailField(blank=True, verbose_name='e-post')
    phone_number = models.CharField(max_length=16, blank=True, verbose_name='telefonnummer')
    birth_date = models.DateField(blank=True, null=True, verbose_name='fødselsdato')

    is_admin = models.BooleanField(default=False, verbose_name='er admin')

    USERNAME_FIELD = 'username'

    objects = MemberManager()

    def __str__(self):
        return self.get_short_name()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.username

    def is_staff(self):
        return self.is_admin

    def is_active(self):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Group(models.Model):
    class Meta:
        verbose_name = 'gruppe'
        verbose_name_plural = 'grupper'

    name = models.CharField(unique=True, max_length=50, verbose_name='navn')
    users = models.ManyToManyField(Member, related_name='groups')
    is_admin = models.BooleanField(default=False, verbose_name='er admin')

    def __str__(self):
        return self.name


class GroupMembership(models.Model):
    member = models.ForeignKey(Member)
    group = models.ForeignKey(Group)


class GroupMembershipPeriod(models.Model):
    membership = models.ForeignKey(GroupMembership)
