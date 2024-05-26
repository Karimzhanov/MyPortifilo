from django.db import models

# Create your models here.


        
class Secondary(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )
    yearsexper = models.IntegerField(
        verbose_name = "Опыт работы пользователя"
    )
    projectfinish = models.IntegerField(
        verbose_name = "Проекты завершенный"
    )
    happyclients = models.IntegerField(
        verbose_name = "Счастливые клиенты"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Доп информации"
        verbose_name_plural = "Доп информации"
   
       
class Colleagues(models.Model):
    full_name = models.CharField(
        max_length = 255,
        verbose_name = "Имя коллеги"
    )
    degree = models.CharField(
        max_length = 255, 
        verbose_name = "Должность"
    )
    company = models.CharField(
        max_length = 255,
        verbose_name = "В каком компании работает"
    )
    photo = models.ImageField(
        upload_to = "colleagues/",
        verbose_name = "Фото коллеги"
    )   
    description = models.CharField(
        max_length = 255, 
        verbose_name = "О коллеге (Как он вам помогает)"
    )    
    def __str__(self):
        return self.full_name 
    class Meta:
        verbose_name = "Информация о коллег"
        verbose_name_plural = "Информация о коллег" 


class Blogs(models.Model):
    name_blog= models.CharField(
        max_length = 255,
        verbose_name = "Имя вашего блога"    
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    image = models.ImageField(
        upload_to = "blogs/",
        verbose_name = "Фото блога" 
    )
    created_at = models.DateField(
        auto_now_add = True,
        blank = True, null = True
    )
    def __str__(self):
        return self.name_blog 
    class Meta:
        verbose_name = "Мои блоги"
        verbose_name_plural = "Мои блоги"
   
   
class PersentShow(models.Model):
    name_thing = models.CharField(
        max_length = 255,
        verbose_name = "Какие библиотеки или фреймфорки он знает"
    )
    persent = models.CharField(
        max_length = 255,
        verbose_name = "На сколько процентов знает"
    )
    logo = models.ImageField(
        upload_to= "persent_show/",
        verbose_name= "Логотип фреймфорка"
    )
    def __str__(self):
        return self.name_thing 
    class Meta:
        verbose_name = "Фреймфорки и скилы я знаю"
        verbose_name_plural = "Фреймфорки и скилы я знаю"
        
        
        
class Projects(models.Model):
    name = models.CharField(
        max_length = 255, 
        verbose_name = "Имя проекта"
    )
    type_job = models.CharField(
        max_length = 255, 
        verbose_name = "Какой тип работы"
    )
    image = models.ImageField(
        upload_to="project/"
    )
    description = models.TextField(
        verbose_name = "Коротко о проекте"
    )
    def __str__(self):
        return self.name   
    class Meta:
        verbose_name = "Мои проекты"
        verbose_name_plural = "Мои проекты"