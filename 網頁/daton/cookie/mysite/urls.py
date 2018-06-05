from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^about$', views.aboutus, name='aboutus'),
    url(r'^products$', views.products, name='aboutus'),
    url(r'^productsdetail$', views.products_detail, name='aboutus'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^send$', views.send, name='send'),
    url(r'^q&a$',views.qa,name='q&a')


    
    

]