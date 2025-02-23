from django.shortcuts import render,redirect

def userReg(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        uname=request.POST['uname']
        psw=request.POST['password']
        cnf_psw=request.POST['cnf_password']
        if cnf_psw==psw:
            data=Udesers.objects.create(name=name,email=email,uname=uname,psw=psw)
            data.save()
        else:
            print('password doesnt match')
    return render (request,'register.html')

def userlogin(request):
    if request.method=='POST':
        uname=request.post['uname']
        psw=request.POST['psw']
        try:
            data=Users.objects.get(psw=psw)
            return redirect(index)
        except:
            return redirect(userlogin)
    return render(request,'login.html')

def index(request):
    return render (request,'index.html')



# Create your views here.
