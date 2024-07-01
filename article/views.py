from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt 
from django.http import HttpResponse
from .models import ArticleColumn, ArticlePost#, ArticleTag
from .forms import ArticleColumnForm, ArticlePostForm#, ArticleTagForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

@login_required(login_url='/account/login/') 
@csrf_exempt

def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user) 
        column_form = ArticleColumnForm()
        return render(request, "article/column/article_column.html", {"columns":columns, 'column_form':column_form})
    
    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name) 
            return HttpResponse("1")

@login_required(login_url='/account/login') 
@require_POST
@csrf_exempt
def rename_article_column(request):
    column_name = request.POST["column_name"] 
    column_id = request.POST['column_id'] 
    print(request.POST)
    try:
        line = ArticleColumn.objects.get(id=column_id) 
        line.column = column_name 
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")

@login_required(login_url='/account/login') 
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST["column_id"] 
    try:
        line = ArticleColumn.objects.get(id=column_id) 
        line.delete()
        return HttpResponse("1") 
    except:
        return HttpResponse("2")
    

@login_required(login_url='/account/login') 
@csrf_exempt
def article_post(request):
    if request.method=="POST":
        article_post_form = ArticlePostForm(data=request.POST) 
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data 
            try:
                new_article = article_post_form.save(commit=False) 
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                # tags = request.POST['tags']
                # if tags:
                #     for atag in json.loads(tags):
                #         tag = request.user.tag.get(tag=atag)
                #         new_article.article_tag.add(tag)
                return HttpResponse("1") 
            except Exception  as e:
                print(e)
                return HttpResponse("2") 

        else:
            return HttpResponse("3")
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        article_tags = ''  #request.user.tag.all()
        return render(request, "article/column/article_post.html",{"article_post_form":article_post_form, "article_columns":article_columns, "article_tags":article_tags})



@login_required(login_url='/account/login') 
def article_list(request):
    articles_list = ArticlePost.objects.filter(author=request.user)
    return render(request, "article/column/article_list.html",{"articles":articles_list })


# def get_absolute_url(self): 
#     return reverse("article:article_detail", args=[self.id, self.slug])

@login_required(login_url='/account/login') 
def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request, "article/column/article_detail.html", {"article":article})