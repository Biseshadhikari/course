from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    courses = Course.objects.all()
    return render(request,'index.html',{
        'courses':courses
    })


def course(request,slug):
    course_detail = Course.objects.get(slug=slug)
    if course_detail.is_verified == True:
        lessons = course_detail.lessons.all()
        return render(request,'coursedetail.html',{
            'id':id,
            'lessons':lessons
        })
    else:
        
        return redirect('/checkout/'+course_detail.slug)

def checkout(request,slug):
    course = Course.objects.get(slug = slug)
    if not course.is_verified:
        if request.method =='POST':
                password = request.POST.get('password')
                if password == course.password:
                    course.is_verified = True
                    course.save()
                    return redirect('/course/'+course.slug)
                else:
                    messages.error(request, 'wrong password')
                    return redirect('/checkout/'+course.slug)
        else:

                return render(request,'checkout.html',
                        {'slug':slug,
                        })
    
    return redirect('/')

