from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    last_name = models.CharField('Фамилия', max_length=512)
    first_name = models.CharField('Имя', max_length=512)
    phone = models.CharField('Телефон', max_length=64, validators=[RegexValidator(
        regex=r'\+7\-\([0-9]{3}\)\-[0-9]{3}\-[0-9]{4}'
    )])
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
