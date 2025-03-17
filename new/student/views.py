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
    data=0  # The purpose of this code is to find a record in the list l that matches the given id and store it in data.
            # t is extracting to give autofill in update.html input field

    for i in l:  #Iterates through the list l, which contains student records as dictionaries.
        if id==i['id']: #Checks if the current dictionary (i) has an "id" that matches the given id.
            data=i
    if request.method=='POST':   #it is for retrieve the submitted data in update.html form
        no=int(request.POST['no'])#When the user submits a form on the update page (update.html), it sends the updated values as a POST request.
        name=request.POST['name'] # The code extracts the new values from request.POST and updates the record in the database or list.
        age=int(request.POST['age'])# It ensures that id and age are converted to integers, preventing data type mismatches.
        email=request.POST['mail']
        cls=int(request.POST['class'])
        subject=request.POST['sub']
        for i in l:
            if id==i['id']:      # 25 - 40 working for send or add details back in list after updating or editing in update field
                i['id']=no        #Finds and updates only the correct record → Ensures that other records remain unchanged
                i['name']=name  #Updates all fields in one step → Prevents data inconsistency.
                i['age']=age  #Allows editing existing data dynamically → Helps manage updates in a user-friendly way.
                i['email']=email
                i['class']=cls
                i['subject']=subject

   
                return redirect(management)

    return render(request,'update.html',{'data':data}) #here data giving for autofill the update input field

def delete(request,id):
    # data2=0
    
    for i in l:
        if id==i['id']:       # if we remove coomented and make comment return redirect then if we delete in browser window
            # data2=i         #then it show deleted details in delete html page in browser as dictionary
            l.remove(i)
            return redirect(management)

    return render(request,'delete.html')#,{'data':data2})



