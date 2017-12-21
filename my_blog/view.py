from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
def hello(request):
	return HttpResponse("Hello world!")
def detail(request,my_args):
	return HttpResponse("You're looking at my_args %s." % my_args)
	"""post = Article.objects.all()[int(my_args)]
        str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
        return HttpResponse(str)"""
def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})
