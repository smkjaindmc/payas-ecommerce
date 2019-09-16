from django.conf.urls import url
from .import views
from products.models import Product
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^fruits/',views.shakes),
    url(r'^fruit/',views.fruit,name='fruit'),
    url(r'^about/',views.about,name='about'),
    url(r'^reviews/',views.review,name='reviews'),
    url(r'^forms/',views.register,name='add'),
    url(r'^user/',views.adduser,name='adduser'),
    url(r'^contact/',views.login_view,name='contact'),
    url(r'^signup/',views.register_view,name='signup'),
    url(r'^menu/',views.menu,name='menu'),
    url(r'^test/',views.test,name='test'),
   url(r'^products/(?P<slug>.*)/$',views.single,name='single-toy'),
    url(r'^cart/',views.carts,name='carts'),
    url(r'^cart/(?P<slug>.*)/$',views.delete,name='delete'),
    url(r'^rewards',views.reward,name='reward'),
    url(r'^prof',views.profile,name='prof'),
    url(r'^ship',views.ship,name='ship'),
    url(r'^addcustomer',views.addcustomer,name='addcustomer'),
    url(r'^branch',views.branch,name='branch'),
    url(r'^cont',views.cont,name='cont'),
    url(r'^test2',views.test2,name='test2'),
    url(r'^logout',views.logout_view,name='logo'),
    url(r'^error',views.error,name='error'),
    url(r'^login',views.login_view,name='contact'),
    url(r'^handlerequest/',views.handlerequest,name='HandleRequest'),
    
]