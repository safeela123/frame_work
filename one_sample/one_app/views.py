from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def fun1(request):
    return HttpResponse("welcome to django")

def fun2(request):
    return HttpResponse("fun2")

def fun3(request,name):
    return HttpResponse("hlo"+name)

def fun4(request,age):
    return HttpResponse("age is"+str(age))

def fun5(request,a,b,c):
    if a>b:
        if a>c:
            return HttpResponse("largest"+str(a))
        else:
            return HttpResponse("largest"+str(c))
    else:
        if b>c:
            return HttpResponse("largest"+str(b))
        else:
            return HttpResponse("largest"+str(c))
        
def fun6(request):
    return render(request,'page.html')

def fun7(request,c):
        a={'name':'manu','age':22,'class':6}
        b=c
        return render(request,'fun7.html',{'data':a,'data1':b})
def fun8(request):
    l=[{'name':'sonu','age':22},{'name':'ravi','age':34}]
    return render(request,'fun8.html',{'data':l}) # data is which given in html page

l=[{'name':'manu','age':33}] # it have to put out of fn bcs of when it will inside of fn then l will be rrturn to it's starting position when redirect
def fun9(request):
   
    if request.method =='POST':
        name=request.POST['a']
        age=int(request.POST.get('b'))
        l.append({'name':name,'age':age}) #here 'name' and 'age' represent keys of dic.
        return redirect(fun9)
    return render(request,'fun9.html',{'data':l})

abw_30=[]
blw_30=[]
def fun10(request):
    if request.method=='POST':
        x=request.POST['n']
        y=int(request.POST['a'])
        if y<=30:
            blw_30.append({'name':x,'age':y})
        else:
            abw_30.append({'name':x,'age':y})

    return render(request,'fun10_split_table.html',{'data1':blw_30,'data2':abw_30})







