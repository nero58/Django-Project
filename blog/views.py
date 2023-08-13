from django.shortcuts import render
from .models import Post


# posts = [
#     {
#         'author': 'Core',
#         'title':'Blog Postl',
#         'content': 'First Post',
#         'date_posted':'24tj Ausgust 2025'
#     },
#     {
#         'author': 'joe',
#         'title':'Blog Pastfsd',
#         'content': 'second Post',
#         'date_posted':'25th Ausgust 2025'
#     }
# ]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context,)


def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

