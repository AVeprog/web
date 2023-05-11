from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
import json

from firstapp.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'contents']


def index(request):
    return render(request, "firstapp/index.html")


def about(request):
    return render(request, "firstapp/about.html")


def contact(request):
    return render(request, "firstapp/contact.html")


#def cart(request):
 #   return render(request, "firstapp/cart.html")


def feedback(request):
    return render(request, "firstapp/feedback.html", context={
        'comment': CommentForm()
    })


def valid(request):
    return render(request, "firstapp/valid.html")


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(json.loads(request.body))
        if form.is_valid():
            Comment.objects.create(**form.cleaned_data)
            return HttpResponse("Created")
        else:
            return HttpResponse("Bad Request", status=400)
    else:
        return HttpResponse("Bad method", status=400)


def get_comment(request):
    comments = Comment.objects.all()
    result = []
    for comment in comments:
        result.append({
            'email': comment.email,
            'contents': comment.contents
        })
    return HttpResponse(json.dumps(result))
