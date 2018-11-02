from goods.models import Category
from show.models import article, Class


def all_show1(request):
    cates = Category.objects.all()
    essaies = article.objects.all()
    all_class = Class.objects.all()

    return cates, essaies, all_class