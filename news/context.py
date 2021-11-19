from news.models import Genre

def category_all(request):
    return {
        "category":Genre.objects.all()
    } 