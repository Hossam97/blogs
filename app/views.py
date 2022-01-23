from django.shortcuts import render
from .models import Articles
from django.contrib.auth.decorators import login_required
from accounts.forms import ArticleForm


@login_required
def create_article(request):
    form = ArticleForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
        context['form'] = ArticleForm()
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # print(title, content)
        # article_object = Articles.objects.create(title=title, content=content)
        # context['object'] = article_object
        # context['created'] = True
        # print(context)
    return render(request, "articles/create.html", context=context)


def search_article(request):

    query = int(request.GET.get('q'))
    article_object = Articles.objects.get(id=query)

    context = {
        "article_object": article_object
    }
    return render(request, "articles/search.html", context=context)


def article_details(request, id=None):
    print(request.user)
    article_object = Articles.objects.get(id=id)
    context = {
        "object": article_object,
        "id": article_object.id,
        "title": article_object.title,
        "content": article_object.content,
        "date": article_object.date,
        "time": article_object.time
    }
    return render(request, "articles/detail.html", context=context)