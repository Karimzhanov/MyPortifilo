from django.shortcuts import render
from apps.telegram.views import get_text
from apps.contacts.models import Contacts
from apps.base.models import InfoUser, Skills, MyService, Education
from apps.secondary.models import Secondary, Colleagues, Blogs, PersentShow, Projects
from apps.base.models import InfoUser
from datetime import datetime

def index(request):
    projects = Projects.objects.all()
    blogs = Blogs.objects.all()
    colleagues = Colleagues.objects.all()
    persent = PersentShow.objects.all()
    skills = Skills.objects.all()
    myservice = MyService.objects.all()
    education = Education.objects.all()
    infouser = InfoUser.objects.latest("id")
    secondary = Secondary.objects.latest("id")
    
    if request.method == "POST":
        name = request.POST.get('fname')
        first_name = request.POST.get('lname')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        service = request.POST.get('service')
        subject = request.POST.get('message')

        contacts = Contacts.objects.create(
                name=name, 
                first_name=first_name, 
                email=email, 
                number=number, 
                service=service,
                subject=subject
            )
          
        get_text(f"""
                Оставлена заявка на заказ

Дата:  {datetime.now()}
Имя пользователя:  {name}
Фамилия пользователя: {first_name}
Почта пользователя: {email}
Номер телефона:  {number}
Услуга: {service}
Сообщение: {subject}
""")

    # Здесь остальной код для получения данных для отображения в шаблоне
    return render(request, "index.html", locals())

def blog_details(request, id):
    blogs = Blogs.objects.get(id=id)
    infouser = InfoUser.objects.latest("id")
    return render(request, "blog-details.html", locals())
