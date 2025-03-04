from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
l=[]

def management(request):
    if request.method =='POST':
        a=int(request.POST['no'])
        b=request.POST['name']
        c=int(request.POST['age'])
        d=request.POST['mail']
        e=int(request.POST['class'])
        f=request.POST['sub']
        # print(a,b,c,d,e,f)
        l.append({'id':a,'name':b,'age':c,'email':d,'class':e,'subject':f})
        return redirect(management)
    return render(request,'std.html',{'data1':l})
def update(request,id):
    data=0
    for i in l:
        if id==i['id']:
            data=i
    if request.method=='POST':   #it is for link the input type in html page
        no=int(request.POST['no'])
        name=request.POST['name']
        age=int(request.POST['age'])
        email=request.POST['mail']
        cls=int(request.POST['class'])
        subject=request.POST['sub']
        for i in l:
            if id==i['id']:      # 25 - 40 working for send or add details back in list after updating or editing in update field
                i['id']=no
                i['name']=name
                i['age']=age
                i['email']=email
                i['class']=cls
                i['subject']=subject

   
                return redirect(management)

    return render(request,'update.html',{'data':data})

def delete(request,id):
    # data2=0
    
    for i in l:
        if id==i['id']:       # if we remove coomented and make comment return redirect then if we delete in browser window
            # data2=i         #then it show deleted details in delete html page in browser as dictionary
            l.remove(i)
            return redirect(management)

    return render(request,'delete.html')#,{'data':data2})



