from idlelib.autocomplete import FILES

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
import Mark1
from Mark1.models import login, sent


def home(request):
    return render(request,'index.html')


def Introducation(request):
    return render(request,'introducation.html')


def Deatils(request):
    if request.method == 'POST':
        select1 = request.POST['slt']
        msg1 = request.POST['tamil']
        time = request.POST['lname']
        date = request.POST['sname']
        check = request.POST['name']
        txtarea1s = request.POST['english']
        select2 = request.POST['slt2']
        txtarea3 = request.POST['txt3']
        txtarea4 = request.POST['txt4']
        reg = sent()
        reg.select = select1
        reg.message = msg1
        reg.date = date
        reg.times = time
        reg.checkbox = check
        reg.message1 = txtarea1s
        reg.slt2 = select2
        reg.message2 = txtarea3
        reg.message3 = txtarea4
        reg.save()
    return render(request,'deatils.html')


def Sent(request):
    data = sent.objects.all()
    context = {'data': data}
    return render(request,'Save.html',context)

def Registeration(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['names']
        email = request.POST['email']
        phone = request.POST['num']
        passwords = request.POST['password']
        reg = login()
        reg.userid = name
        reg.lastname = lastname
        reg.email = email
        reg.phone = phone
        reg.password = passwords
        reg.save()
    return render(request,'Registeration.html')




def Loginpage(request):

    if request.method == 'POST':
        context_id = ''
        context_password = ''

        userid = request.POST['uname']
        password = request.POST['psw']
        data = login.objects.filter(userid=userid)
        if len(data) == 0:
           context_id = 'User does not exist!!'
           context_password = ''
        else:
            if password ==(data[0].password):

                context = {
                    'user1': data[0].userid,
                }
                return render(request, 'logged.html',context)
            else:
                context_id = ''
                context_password = 'your user id (or) password not matching...! '

        context = {
            'id': context_id,
            'password': context_password
        }

        return render(request, 'loginpage.html', context)
    else:
        context = {
            'id': '',
            'password':''

        }
    return  render(request,'loginpage.html',context)



def Save(request):
        data = login.objects.all()
        context = {'data': data}
        return render(request,'Sent.html',context)

        # if request.method == "GET":
           #       name = request.GET.get('tamil')
           #       x = str(name)
           #      data = login.objects.all().filter(Q(userid__icontains=x))
           #     context = {'data': data}
           #     return render(request,'Sent.html',context),


def Other(request):
    return render(request,'Other.html')




def Logged(request):
    return render(request,'logged.html')


def Loginout(request):
    return render(request,'loginout.html')