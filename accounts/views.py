from django.shortcuts import render, redirect
from django.http import HttpResponse

from accounts.forms import AccountForm
from accounts.models import PersonAccount

from django.contrib import messages

from django.http import StreamingHttpResponse
import cv2
import threading

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def home(request):
    context = {'test':'test'}
    return render(request, 'accounts/home.html', context)


def livesetup(request):

    context = {'test':'test'}
    return render(request, 'accounts/livepage.html', context)

def livepage(request):

    context = {'test':'test'}
    return render(request, 'accounts/livepage2.html', context)



def login(request):
    print('Login')
    context = {'test':'test'}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = PersonAccount(email=email,password=password)
        print(f"Account = {user}")
        if email is None or email == "" or password is None or password == "":
            if email is None or email == "":
                print('Email Empty')
                messages.error(request, 'Email field cannot be empty.')
            if password is None or password == "":
                print('Password Empty')
                messages.error(request, 'Password field cannot be empty.')
        elif user is not None:
            print(f'User: {user} has successfully login.')
            return redirect('home')
        else:
            print('Failed')
            messages.error(request, 'Invalid Account')
    return render(request,'accounts/login.html', context)

def signup(request):
    notificationText = ''
    accountForm = AccountForm(use_required_attribute=False)
    if request.method == 'POST':
        accountForm = AccountForm(request.POST, request.FILES,use_required_attribute=False, id='-1')
        print('Add Account.')
        if accountForm.is_valid():
            messages.success(request, 'Sign up Successfully!.')
            accountForm.save()
            context = {'account_form':accountForm,'process':"Add",'output':notificationText,'notification':True}
            return redirect('/signup/')  
        else:
            errlist = ''
            for field in accountForm.errors:
                errlist += f' {field}'

    context = {'account_form':accountForm,'process':"Add",'output':notificationText,'notification':True}
    return render(request, 'accounts/signup.html',context)

def customer(request):
    return HttpResponse('customer')
