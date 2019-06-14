from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.core.mail import send_mail, BadHeaderError, send_mass_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.urls import reverse
from .forms import ContactForm, UserForm, UserProfileInfoForm, ContactForm2
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.core.mail import EmailMessage
from twilio.rest import Client
from django.conf import settings




def index(request):
    return render(request, 'student/base.html')


def loginnext(request):
    return render(request, 'student/loginnext.html')


def smsnext(request):
    return render(request, 'student/sms.html')

def staff(request):
    return render(request, 'student/try.html')


def student(request):
    return render(request, 'student/studentlogin.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
                profile.role = 'student'
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'student/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'student/login.html', {})


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            to_email = [from_email, 'vbranchagi@gmail.com']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, to_email, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "student/email.html", {'form': form})

def tryView(request):
    if request.method == 'GET':
        form = ContactForm2()
    else:
        form = ContactForm2(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['vbranchagi@gmail.com','poojasunkad96@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success3')
    return render(request, "student/email.html", {'form': form})

def tryView2(request):
    if request.method == 'GET':
        form = ContactForm2()
    else:
        form = ContactForm2(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['vbranchagi@gmail.com','poojasunkad96@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success3')
    return render(request, "student/email.html", {'form': form})


def success3(request):
    return render(request, 'student/emailsuccess2.html')


def success(request):
    return render(request, 'student/emailsuccess.html')


def success2(request):
    return HttpResponse('Password Changed Successfully! .')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('success2')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'student/change_password.html', {
        'form': form
    })

def sms(request):
    account_sid = 'AC3ac0c5f267c8421f7541b6fbdc82b789'
    auth_token = '2023bd99104b7fd1287952a8c1861337'
    myPhone = '+917795647663'  # Phone number you used to verify your Twilio account
    TwilioNumber = '+12564488402'  # Phone number given to you by Twilio
    client = Client(account_sid, auth_token)
    client.messages .create(
        to=myPhone,
        from_=TwilioNumber,
        body='Message from Exam Cell -- Results of 2nd/4th/6th Semesters announced -- check at: eresults.kletech.ac.in '
    )
    return render(request, "student/sms.html")



def user_login2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index2'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'student/studentlogin.html', {})

def index2(request):
    return render(request, 'student/base2.html')

def sms(request):
    account_sid = 'AC3ac0c5f267c8421f7541b6fbdc82b789'
    auth_token = '2023bd99104b7fd1287952a8c1861337'
    myPhone = '+917795647663'  # Phone number you used to verify your Twilio account
    TwilioNumber = '+12564488402'  # Phone number given to you by Twilio
    client = Client(account_sid, auth_token)
    client.messages .create(
        to=myPhone,
        from_=TwilioNumber,
        body='Message from Exam Cell -- Results of 2nd/4th/6th Semesters announced -- check at: eresults.kletech.ac.in '
    )
    return render(request, "student/sms.html")
