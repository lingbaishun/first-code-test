# Django学习  
###  一、创建

- **创建项目**
  
	`python django-admin.py startproject projectname`
  
- **在目录下创建app**
  
	`python django-admin.py startapp appname`

###  二、应用

- **添加应用**

    将我们新建的应用添加到 settings.py 中的INSTALLED_APPS中，也就是告诉Django有这么一个应用。
    ```bash
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'polls',
    )
    ```

###  三、修改app中models，设置功能

- **修改模型**
  
  ```bash
  from django.db import models
  from django_bulk_update.manager import BulkUpdateManager
  class Person(models.Model):
  	display_field = ('name', 'age', 'id')
      name = models.CharField(
      	max_length=30,
      	null=False,
      	blank=True,
      	default='小白',
      	verbose_name='姓名')
      age = models.IntegerField(
          max_length=30,
      	null=False,
      	blank=True,
      	default=18
      	verbose_name='年龄')
      is_man = models.BooleanField()
      message = models.TextField()
      
      objects = model.Manager()
      #objects = BulkUpdateManager()
      
      class Meta:
      	managee = False
      	db_table = 'lingbai_table'
      	get_latest_by = 'modified'
      	ordering = ['created']
      	select_on_save = True
      	indexes = [models.Index(fields=['script_id',])]
      	verbose_name = '信息表'
      
      
  ```

###  四、创建数据表

  ```bash
   python manage.py makemigrations
   python manage.py migrate 
  ```

###  五、插入数据

   ```
   Person.objects.create(name=name,age=age)
   p = Person(name="WZ", age=23)
   p.save()
   p = Person(name="TWZ")
   p.age = 23
   p.save()
   Person.objects.get_or_create(name="WZT", age=23)
   ```

###  六、创建视图

   ```
from django.views.generic import View
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, FileResponse
from any_case import converts_keys  #结果关键字转化为驼峰

class Person(View):
	def post(self, request):
	 	username = request.user.username
	 	
	 	args = request.POST.copy()
	 	data = Person.objects.filter(id=id)
	 	paginator = Paginator(data, page_size)
	 	data_out = list(paginator
	 				    .page(page_index)
	 				    .objects
	 				    .vaules(**Person.display_fieleds))
	 	JsonResponse(data_out)
   ```

###  七、定义地址

   ```
from django.conf.urls import url
from .api.views import Person

urlpatterns = [
	url(r'^list/person$',
		Person.as_view(),
		name='人'),
]
   ```