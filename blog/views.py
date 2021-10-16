from django.shortcuts import redirect,render
from .models import Blog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .form import AddCommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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
    try:
      prev = get_object_or_404(Blog, pk=(detail.id)-1)
    except:
      prev = None

    try:
      next = get_object_or_404(Blog, pk=(detail.id)+1)
    except: 
      next = None

    return render(request, 'blog/blog_detail.html',{'detail':detail,'prev':prev,'next':next})


@login_required
def add_comment(request):
  if request.method == 'POST':
    form = AddCommentForm(request.POST )
    if form.is_valid():
        myform=form.save(commit=False)
        myform.name=request.user
        myform.save()
        return redirect(reverse('blog/blog_detail.html'))

  else:
    form=AddCommentForm()
    context= {'formm':form}
    return render(request,'blog/blog_detail.html',context)
