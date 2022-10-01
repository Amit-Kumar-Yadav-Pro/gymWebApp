from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
#    data={
#        'name':'Amit Yadav',
#        'Biodata':'Information Technology',
#        'Learned':['PHP', 'Java Script', 'python'],
#        'student_details':[
#            {'name':'Amit Yadav','mobile':888239638},
#            {'name':'Sumit Yadav','mobile':783869638},
#            {'name':'Karan Yadav','mobile':9934990050},
#            {'name':'Umesh Yadav','mobile':7845129865}
#            ]
#    }
    return render(request, "home.html");

def shop(request):
    return render(request, "Shop.html");

def about(request):
    return render(request, "About.html");
    
def contact(request):
    return render(request, "Contact.html");

def blog(request):
    return render(request, "Blog.html");

def blogDetails(request, blog_title):
    return HttpResponse ( "Blog Page -  " + blog_title);
