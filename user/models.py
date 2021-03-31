from django.db import models


# Create your models here.
class User(models.Model):
    gender_choice = ((0, 'girl'), (1, 'boy'))
    userId = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=64, verbose_name='', blank=True)
    account = models.CharField(max_length=32, verbose_name='')
    password = models.CharField(max_length=128, verbose_name='')
    phone = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=64, blank=True)
    sex = models.SmallIntegerField(choices=gender_choice, blank=True)
    createDate = models.DateTimeField(auto_now_add=True, blank=True)
    updateDate = models.DateTimeField(auto_now=True, blank=True)
    isDel = models.SmallIntegerField(default='0')

    def user_to_dict(self):
        return {
            'name': self.name,
            'account': self.account,
            'phone': self.phone,
            'address': self.address,
            'email': self.email,
            'sex': self.sex,
            'createDate': self.createDate,
            'updateDate': self.updateDate,
            'isDel': self.isDel
        }
