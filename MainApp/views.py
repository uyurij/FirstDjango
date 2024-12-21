from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home(request):
    context = {
        "name": "Горбунов Юрий Геннадьевич",
        "email": "uyurij@yandex.ru"
    }
    return render(request, 'index.html', context)

def about(request):
    text = """
    <p>Имя: <b>Юрий</b><br>
    Отчество: <b>Геннадьевич</b><br>
    Фамилия: <b>Горбунов</b><br>
    Телефон: <b>+7 (906)715-29-02</b><br>
    email: <b>uyurij@yandex.ru</b></p>
    <nav>
    <ul>
      <li><a href="items">Товары</a></li>
      <li><a href="/">Главная</a></li>
    </ul>
  </nav>
    """
    return HttpResponse(text)

def get_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(f"Item with id={id} not found")
    else:
        context = {"item": item}
        return render(request, "item.html", context)
 
def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items,
        "color" : colors,
    }
    return render(request, 'items.html', context)


