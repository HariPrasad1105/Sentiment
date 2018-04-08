from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns =[
                url(r'^$', views.heading, name='index'),
                url(r'login/$', views.redirectlogin, name='login'),
                url(r'signup/$', views.redirectsignup, name='signup'),
                url(r'auth/$', views.authenticate, name='OAuth'),
                url(r'forgot/$', views.forgotpassword, name='forgotpassword'),
                url(r'sendmail/$', views.sendmail, name='sendmail'),
                url(r'otpvalidate/$', views.validateotp, name='validateotp'),
                url(r'auth1/$', views.signupDetails, name = 'signupDetails'),
                url(r'changepassword/$', views.passwordchange, name='passwordchange'),
                url(r'keyword/$', views.keyword, name='keyword'),
                url(r'downloaded/$', views.downloaded, name='downloaded'),
                url(r'sentiment/$', views.sentiment, name='sentiment'),
                url(r'downloaded1/$', views.downloaded1, name='downloaded1'),
                url(r'result/$', views.result, name='result'),
             ]
