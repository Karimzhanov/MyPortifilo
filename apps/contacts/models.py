from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )

    first_name = models.CharField(
        max_length = 255,
       verbose_name = 'Фамилия'
    ) 

    email = models.EmailField(
        verbose_name = 'Почта',
    )

    number = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    
    service = models.TextField(
        verbose_name= 'Услуга'
    )

    subject = models.CharField(
        max_length = 255,
        verbose_name='Сообщение'
    )



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

from django.db import models

class PageContact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )

    first_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия'
    )

    email = models.EmailField(
        verbose_name='Почта'
    )

    number = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )

    subject = models.CharField(
        max_length=255,
        verbose_name='Тема'
    )

    message = models.TextField(
        verbose_name='Сообщение'
    )

    def __str__(self):
        return f"{self.name} {self.first_name}"

    class Meta:
        verbose_name = 'Сообщение на странице'
        verbose_name_plural = 'Сообщения на странице'
