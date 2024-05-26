from django.db import models

# Create your models here.

 
class InfoUser(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя"
    )
    image = models.ImageField(
        upload_to = "info_user/",
        verbose_name = "Фотография пользователя"
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = "Профессия пользователя"
    )
    
    skills = models.CharField(
        max_length = 255,
        verbose_name = "Каким образом пользователь делает работу"
    )
    
    email = models.EmailField(
        max_length = 255,
        verbose_name = "Почта пользователя"
    )
    
    phone_number = models.CharField(
        max_length = 255,
        verbose_name = "Номер телефона"
    )
    
    adress = models.CharField(
        max_length = 255,
        verbose_name = "Адрес"
    )
    
     
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователя"


class MyService(models.Model):
    type_job = models.CharField(
        max_length = 255,
        verbose_name = "Тип работы"
    )
    
    number_service = models.IntegerField(
        verbose_name = "Номер работы (порядок)"
    )
    
    aboutproj = models.CharField(
        max_length = 255,
        verbose_name = "Коротко как я делает роботу"
    )
    
    def __str__(self):
        return self.type_job
    
    class Meta:
        verbose_name = "Мои услуги"
        verbose_name_plural = "Мои услуги"
      
        
class Skills(models.Model):
    
    typedevelop = models.CharField(
        max_length = 255,
        verbose_name = "Какой разработчик"
    )
    
    time = models.CharField(
        max_length = 255,
        verbose_name = "В каком году начал и закончил"
    )
    
    location = models.CharField(
        max_length = 255,
        verbose_name = "Где работал"
    )
    def __str__(self):
        return self.typedevelop
    
    class Meta:
        verbose_name = "Мой опыт"
        verbose_name_plural = "Мой опыт"
        
        
        
class Education(models.Model):
    when_course = models.CharField(
        max_length =255 ,
        verbose_name = "Когда обучался"
    )
    
    where_study = models.CharField(
        max_length = 255, 
        verbose_name = "Где учился"
    )
    course_name = models.CharField(
        max_length = 255,
        verbose_name = "В каком курсе или университе училя"
    )
    def __str__(self):
        return self.where_study
    class Meta:
        verbose_name = "Мое оброзование"
        verbose_name_plural = "Мое оброзование"
      

 
    
   
        
        
 