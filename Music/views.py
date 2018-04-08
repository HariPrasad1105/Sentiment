from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginDetails
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from matplotlib.backends.backend_agg import FigureCanvasAgg
from pylab import figure, axes, pie, title
from wordcloud import WordCloud, STOPWORDS
import sys
import random

path = 'E:\Hackathon\HackathonProject\Music\FirstPythonProject'
sys.path.append(path)

from sentiment import Sentiment1
from TrainingAlgorithm import Algorithm

# Create your views here.


def heading(request):
    return render(request, "home.html", {'name': 'Hari Prasad'})


def redirectlogin(request):
    return render(request, 'login1.html', {'name': 'Hari Prasad'})


def redirectsignup(request):
    return render(request, 'signup1.html')


def authenticate(request):
    postemail = request.POST['emailid']
    try:
        a = LoginDetails.objects.get(email_id=postemail)
    except LoginDetails.DoesNotExist:
        return render(request, 'login1.html', {'error': 'Invalid Input credentials'})
    if a.password == request.POST['password']:
        return render(request, 'authenticate.html', {'username': a.user_name})
    else:
        return render(request, 'login1.html', {'error': 'Invalid Input credentials'})


def forgotpassword(request):
    return render(request, 'forgotpassword.html', {'msg1': 'Request to set password'})


otp = random.randint(1000, 9999)
mail_ = ''


def sendmail(request):
    mail, list1 = request.POST['email'], []
    global mail_
    if mail:
        mail_ = mail
    emailidlist = LoginDetails.objects.filter(email_id=mail)
    if emailidlist:
        msg = 'OTP to set the password is ' + str(otp)
        list1.append(mail)
        send_mail('OTP to reset password', msg, 'hariprasad.jella05@gmail.com', list1)
        return render(request, 'forgotpassword.html',
                      {'msg1': 'OTP has been send to registered email address', 'mail': mail_, 'list': list1,
                       'listofdetails': emailidlist})
    else:
        return render(request, 'forgotpassword.html', {'message1': 'EmailID not found in database.'})


def validateotp(request):
    otp2 = request.POST['otp']
    if otp == int(otp2):
        return render(request, 'passwordchange.html', {'message': 'you can update the password', 'mail': mail_})
    else:
        return render(request, 'forgotpassword.html', {'message': otp == int(otp2)})


def signupDetails(request):
    details = LoginDetails()
    details.email_id, details.password, details.user_name = request.POST['emailid'], request.POST['password'], request.POST['username']
    details.save()
    return render(request, 'login1.html', {'details': details.email_id + details.password + details.user_name})


def passwordchange(request):
    password_, email, confirm_password_ = request.POST['password'], request.POST['emailid'], request.POST[
        'confirm_password']
    if password_ == confirm_password_:
        details = LoginDetails.objects.get(email_id=email)
        details.password = password_
        details.save()
        return render(request, 'login1.html')
    else:
        return render(request, 'passwordchange.html', {'message': 'Passwords Donot Match.'})


def keyword(request):
    return render(request, 'keywordsearch.html')


def downloaded(request):
    return render(request, 'downloaded.html')


pos, neg, neu, wordcloud1 = 0, 0, 0, ""


def sentiment(request):
    global wordcloud1
    keyword_ = request.POST['keyword']
    algo1 = Sentiment1(keyword_)
    algo1.function()
    algo = Algorithm("preprocessed.csv")
    pos, neg, neu, wordcloud1 = algo.result()
    return render(request, 'piechart.html', {'positive': pos, 'negative': neg, 'neutral': neu})


def downloaded1(request):
    global wordcloud1
    keyword_ = request.POST['keyword']
    if keyword_ == 'iphonex':
        algo = Algorithm('iphonex.csv')
    if keyword_ == 's9':
        algo = Algorithm('s9.csv')
    if keyword_ == 'oneplus':
        algo = Algorithm('oneplus.csv')
    if keyword_ == 'macbook':
        algo = Algorithm('macbookpro.csv')
    pos, neg, neu, wordcloud_ = algo.result()
    wordcloud1 = wordcloud_
    return render(request, 'piechart1.html', {'positive': pos, 'negative': neg, 'neutral': neu, 'wordcloud': wordcloud1})



def result(request):
    global wordcloud1
    return render(request, 'sentimentresult.html', {'wordcloud': wordcloud1})
