from django.shortcuts import redirect,render
from .models import Blog , Comment
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import AddCommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import  HttpResponseRedirect


# Create your views here.
def blog (request):
    blogs=Blog.objects.all()

  #  myfilter= JobFilter(request.GET,queryset=blogs)
  #  blogs = myfilter.qs

    paginator = Paginator(blogs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    njob = Blog.objects.all().count() 
   

    return render(request, 'blog/blog.html',{'blogs':blogs,'jobs': page_obj,'Njob':njob})



def blog_details (request ,id):
    detail=Blog.objects.get(id=id)
    comments = Comment.objects.all()
    comm = comments.count()

    try:
      prev = get_object_or_404(Blog, pk=(detail.id)-1)
    except:
      prev = None

    try:
      next = get_object_or_404(Blog, pk=(detail.id)+1)
    except: 
      next = None


    if request.method == 'POST':
      
      form = AddCommentForm(request.POST , request.FILES)
      if form.is_valid():
          myform=form.save(commit=False)
          myform.user=request.user
          myform.blog=detail
          myform.save()
          return HttpResponseRedirect('#')
    else:
      form=AddCommentForm()



    return render(request, 'blog/blog_detail.html',{'detail':detail,'prev':prev,'next':next,'form':form , 'comm':comm,'comments':comments})


