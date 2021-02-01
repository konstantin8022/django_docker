# django_docker
django_docker navigator molodogo edagoga

для данного проекта существует 2 принципа запуска первый с использованием докера, второй с использованием venv. предполагается что человек, который будет заниматься деплоем приложения имеет представление, что такое докер и джанго. 

**Production Deploy.**

на продакшн сервере обязательно занесите переменную в окружение "is_production=1"

export is_production=1

убедитесь в доступности, нужной версии пайтон, а также в том что установлены постгрес, редис, супервизор(по необходимости)

install python >= 3.4, postgress, redis, supervisor, git, nginx

для постгресс нужно создать юзера и базу данных, а также обязательно дать права на базу созданному юзеру

если предполагается использовать супервизор, почитайте ссылки

supervisor: https://ruhighload.com/post/%D0%97%D0%B0%D0%BF%D1%83%D1%81%D0%BA+%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%BE%D0%B2+%D0%B2+supervisor
ps:
http://masnun.rocks/2016/11/02/deploying-django-channels-using-daphne/


**Docker Deploy**

описывать разворачивания докер контейнера, не будем, кроме сноски ** это не должно быть сложно



**Сноска тут**

если вы применяете миграции первый раз, то неизбежно столкнетесь с проблемой:
 "django.db.utils.ProgrammingError: relation "django_content_type" does not exist
LINE 1: ..."."app_label", "django_content_type"."model" FROM "django_co...
"
делаем так:


в settings.py 

INSTALLED_APPS = [
    # 'admin_tools',
    # 'admin_tools.theming',
    # 'admin_tools.menu',
    # 'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'rest_framework',
    # 'oauth2_provider',
    # 'social_django',
    # 'rest_framework_social_oauth2',
    # 'rest_framework_docs',
    # 'rest_framework_swagger',
    # 'drf_autodocs',
    # 'phonenumber_field',
    # 'taggit_serializer',
    # 'taggit',
    # 'votes',
    # 'channels',
    # 'django_filters',
    # 'fcm_django',
    # 'debug_toolbar',

    'navy.applications.users',
    # 'navy.applications.avatars',
    # 'navy.applications.posts',
    # 'navy.applications.comments',
    # 'navy.applications.polls',
    # 'navy.applications.news',
    # 'navy.applications.chats',
    # 'navy.applications.support',
    # 'navy.applications.vacancies',
    # 'navy.applications.resumes',
    # 'navy.applications.about_us',
    # 'navy.applications.important_to_know',
]


и в urls.py urlpatterns = [
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^api/v0/socialauth/', include('rest_framework_social_oauth2.urls')),
    # url(r'^docs/', include('rest_framework_docs.urls')),
    # url(r'^api/v0/', include('navy.api.v0.urls', namespace='v0')),
    # url(r'^fake$', FakeData.as_view(), name='fake'),
    # url(r'^$', AboutView.as_view(), name='index'),
]

затем применяем миграции.

после этого раскоментируйте всё и повторите миграции

после того как миграции будут применены вы можете создавать суперпользовотеля


cd ../project/directory; python manage.py createsuperuser(username='spacebar'+'enter');
python manage.py shell; from navy.applications.users.models import User; u = User.objects.get(email='createduser@some.ru');
u.is_active=True; u.save(); 


всё пользователь создан


**Конец сноски**

**замечания**

счетчик чатов не отслеживает конкретных пользователей. он считает количество подключеных девайсов

пуши отправляются использую channels, если будет нужно найти функцию, которая отправляет пуш, ищите ее в chats
