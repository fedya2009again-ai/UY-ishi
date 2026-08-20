from django.shortcuts import render, redirect
from .forms import CommentForm, PhoneForm
from django.http import HttpRequest

from .models import Phone, Categoory, Comment

def all_phone(request):
    phones = Phone.objects.all()
    categorys = Categoory.objects.all()
    context = {
        "phones":phones,
        "categorys":categorys
    }
    return render(request, 'main/home.html', context)

def by_category(request, category_id):
    category = Categoory.objects.all()
    phone = Phone.objects.filter(category_id=category_id)
    context = {
        'categorys':category,
        'phones':phone
    }
    return render(request, 'main/home.html', context)

def detail(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    comment = Comment.objects.filter(phone_id=phone_id)
    context = {
        'phone':phone,
        'comment':comment
    }
    return render(request, 'main/detail.html', context)

def create_phone(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = PhoneForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                phone = form.save()
                return redirect('detail', phone_id=phone.id)
        else:
            form = PhoneForm()
        context = {
            'form':form
        }
        return render(request, 'main/add_book.html', context)

    else:
        return redirect('home')


#----------------- Comment ----------------------
def save_comment(request: HttpRequest, phone_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
           form = CommentForm(data=request.POST)
           if form.is_valid():
                phone = Phone.objects.get(id=phone_id)
                comment = Comment.objects.create(text=form.cleaned_data.get("text"), phone=phone, user=request.user)
           else:
               print('simvollar soni 500 tadan kop')
           return redirect('detail', phone_id=phone_id)
        else:
            return redirect('all_phone')
    else:
        print('login qiling')
        return redirect('all_phone')


def update_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user.is_authenticated and request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                comment.text = form.cleaned_data.get("text")
                comment.save()
                return redirect('detail', phone_id=comment.phone.id)
        else:
            form = CommentForm(initial={"text": comment.text})
        context = {
            "form": form
        }

        return render(request, "main/comment_update.html", context)
    else:
        print('login qiling')
        return redirect('home')


def delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user.is_authenticated and request.user == comment.user or request.user.is_superuser:
        phone_id = comment.phone.id
        if request.method == "POST":
            comment.delete()
            return redirect('detail', phone_id=phone_id)
        else:
            return render(request, 'main/coniform_delete.html', {"comment": comment})
    else:
        print('login qiling')
        return redirect('home')










