from django.contrib import admin
from apps.secondary.models import Secondary, Colleagues,  PersentShow, Blogs, Projects

# from django.contrib.auth.models import User, Group

# Register your models here.

admin.site.register(Secondary)
admin.site.register(Colleagues)
admin.site.register(PersentShow)
admin.site.register(Projects)
admin.site.register(Blogs)

# admin.site.unregister(User)
# admin.site.unregister(Group)