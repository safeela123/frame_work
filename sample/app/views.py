from django.shortcuts import render,redirect
from django.http import HttpResponse  # this is importing to write mesage to show in display


# Create your views here.

# def fun1(request):  # these fn1-fn5 is for pass message by urls passing
#     return HttpResponse("welcome to django") # here will message will write which have to display


    

# def fun2(request):
#     return HttpResponse("fun2")

# def fun3(request,name):
#     return HttpResponse("fun3"+name)

# def fun4(request,age):
#     return HttpResponse("fun4"+str(age))  # have to convert an integer  into string bcs can't work string and integer at single string.
#                                             #call these fn in urls which is in project foler here sample folder

# def fun5(request,a,b,c):
#     if a>b:
#         if a>c:
#             return HttpResponse("largest"+str(a))
#         else:
#             return HttpResponse("largest"+str(c))
#     else:
#         if b>c:
#             return HttpResponse("largest"+str(b))
#         else:
#             return HttpResponse("largest"+str(c))
        
# def fun6(request):  #this fn for pass urls for pass an html page
#     return render(request,'index.html') #here giving html page here

# def fun7(request,c):
#     a={'name':'manu','age':22}
#     b=c
#     return render(request,'index.html',{'data':a,'data1':b})

# def fun8(request):
#     l=[{'name':'manu','age':22},{'name':'anu','age':20},{'name':'vinu','age':30}]
#     return render(request,'index.html',{'data':l})
# l=[{'name':'anu','age':33},{'name':'manu','age':23},{'name':'thanu','age':13}]
# def fun9(request):
#     if request.method=='POST':
#         # print(request.POST)
#         name=request.POST['name'] # d[age]
#         age=request.POST.get('age') # d.get(age)
#         print(name,age)
#         l.append({'name':name,'age':age}) # here name and age are name which gave in html page for input types
#         return redirect(fun9) # it is for avoid error when refresh page
#     return render(request,'index.html',{'data':l})


blw_30=[]
abv_30=[]
def fun10(request):
    
    if request.method=='POST':
            name=request.POST['name']
            age=int(request.POST['age'])
            print(name,age)
            if age>30:
                    abv_30.append({'name':name,'age':age})
                    return redirect(fun10)
            if age<=30:
                    blw_30.append({'name':name,'age':age})
                    return redirect(fun10)
    return render(request,'split_table.html',{'data':abv_30,'data1':blw_30})
    
# def ele_city(request):
#         if request.method=='POST':
#                   value=int(request.POST['unit'])
#                 if value<=100:
#                         print("no charge")
#                         return render(request,'index.html')
          
