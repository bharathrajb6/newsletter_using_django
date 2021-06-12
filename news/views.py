from django.shortcuts import render, redirect
import smtplib
from django.contrib import messages
from news.models import feeds
import random as ra
import string


def home(request):
    obj = feeds.objects.all()

    obj2 = obj[0:4]
    return render(request, 'home.html', {'data': obj2})


def about(request):
    return render(request, 'about.html')


def content(request):
    if request.method == "POST":
        fid = request.POST['fid']
        obj = feeds.objects.get(fid=fid)
        return render(request, 'detail.html', {'data': obj})
    else:
        obj = feeds.objects.all()
        return render(request, 'content.html', {'data': obj})


def academics(request):
    obj = feeds.objects.filter(category='Academics')
    return render(request, 'content.html', {'data': obj})


def sports(request):
    obj = feeds.objects.filter(category='Sports')
    return render(request, 'content.html', {'data': obj})


def management(request):
    obj = feeds.objects.filter(category='Management')
    return render(request, 'content.html', {'data': obj})


def culture(request):
    obj = feeds.objects.filter(category='Culture')
    return render(request, 'content.html', {'data': obj})


def add_news(request):
    N = 7
    if request.method == "POST":
        title = request.POST['title']
        category = request.POST['category']
        sub = request.POST['sub']
        desc = request.POST['desc']
        date = request.POST['date']
        fid = ''.join(ra.choices(string.ascii_uppercase + string.digits, k=N))
        obj = feeds(fid=fid, category=category, title=title, subtitle=sub, desc=desc, time=date)
        obj.save()
        messages.success(request, 'Successfully added')
        return redirect('admin_menu')
    else:
        return render(request, 'add_news.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['message']
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("bharathsr2001@gmail.com", "Bharath@B26")
            message = "Contact \n\nName : {}\nEmail : {}\nTelephone : {}\n{}".format(name, email, phone, msg)
            s.sendmail(email, "bharathsr2001@gmail.com", message)
            s.quit()
            messages.success(request, 'Successfully Sent')
            return redirect('home')
        except:
            messages.success(request, 'Unable to Sent')
            return redirect('home')
    else:
        return render(request, 'contact.html')


def admin_login(request):
    if request.method == "POST":
        user = request.POST['username']
        pass1 = request.POST['password']
        if user == 'admin' and pass1 == '4su18cs017':
            messages.success(request, 'Welcome Admin')
            return redirect('admin_menu')


    else:
        return render(request, 'admin_login.html')


def admin_menu(request):
    obj = feeds.objects.all()
    return render(request, 'admin_menu.html', {'data': obj})


def edit_news(request):
    if request.method == "POST":
        fid = request.POST['fid']
        obj = feeds.objects.get(fid=fid)
        return render(request, 'edit.html', {'data': obj})


def delete_news(request):
    if request.method == "POST":
        fid = request.POST['fid']
        obj = feeds.objects.get(fid=fid)
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('admin_menu')


def edit_details(request):
    if request.method == "POST":
        fid = request.POST['fid']
        category = request.POST['category']
        title = request.POST['title']
        desc = request.POST['desc']
        time = request.POST['time']
        obj = feeds.objects.get(fid=fid)
        obj.category = category
        obj.title = title
        obj.desc = desc
        obj.time = time
        obj.save()
        messages.success(request, 'Updated Successfully')
        return redirect('admin_menu')
