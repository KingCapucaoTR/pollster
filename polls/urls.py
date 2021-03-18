from django.urls import path # routes

from . import views # import all

app_name = 'polls' #namespace

# arrays of urls/routes
urlpatterns = [
    path('', views.index, name='index'), # '' means /polls route -- root --if you add say 'result' it will be polls/result
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test/', views.test, name='test')
]

