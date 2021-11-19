from news.models import Category

def category_all(request):
    return {
        "category":Category.objects.all()
    } 