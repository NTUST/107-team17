from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.aboutus, name='aboutus'),
    url(r'^products$', views.products, name='aboutus'),
    url(r'^productsdetail$', views.products_detail, name='aboutus'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^send$', views.send, name='send'),
    url(r'^q&a$',views.qa,name='q&a'),
    url(r'^englishver$',views.english,name='english'),
    url(r'^news$',views.news,name='news'),
    url(r'^noproblem$',views.noproblem,name='noproblem'),
    url(r'^question$',views.question,name='question'),
    url(r'^tictactoe$',views.tictactoe,name='tictactoe'),
    url(r'^newsgraduate$',views.newsgraduate,name='newsgraduate'),





    
    

]