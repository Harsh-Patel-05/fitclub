from django.shortcuts import render,redirect
from myapp.models import deficiency, exercise, item, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def exercises(request):
    uid = request.session['log_id']
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    getexercise = exercise.objects.all().filter(de_id=deffid)
    print(getexercise)
    return render(request, 'exercise.html', {'exercises': getexercise})

def loginpage(request):
    return render(request, 'registration/login.html')

def register(request):
    fetchdef = deficiency.objects.all()
    return render(request, 'registration/register.html', {'def': fetchdef})

def viewdata(request):
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        gender = request.POST.get("gender")
        defid = request.POST.get("Deficiency")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("number")

        logindata = login(firstname=firstname, lastname=lastname,address=address, age=age, height=height, phone_no=phone, weight=weight,
                          gender=gender, de_id=deficiency(id=defid), email_id=email, password=password, role=2,
                          status=1)
        logindata.save()
        messages.success(request, 'Data Inserted Successfully. you can login now')
        return render(request, 'registration/login.html')
    else:
        messages.error(request, 'error occured')
        print("errrorrr")

    return render(request, 'registration/login.html')

def checklogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = login.objects.get(email_id=email, password=password)
            request.session['log_user'] = user.email_id
            request.session['log_id'] = user.id
            request.session.save()
            fetchitem = item.objects.all()[0:8]
            print(fetchitem)

        except login.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'index.html', {'products': fetchitem})

        else:
            messages.info(request, 'account does not exit plz sign in')
    return render(request, 'index.html')

def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_id']
    except:
        pass
    return redirect('login.html')
    # return render(request, 'registration/login.html')