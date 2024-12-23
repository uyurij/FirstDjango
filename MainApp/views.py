from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 1, "name": "Куртка кожаная", "quantity": 2},
    {"id": 1, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 1, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


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

def get_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponse(f"Item with id={item_id} not found")
    else:
        context = {"item": item}
        return render(request, "item.html", context)
 
def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items,
       #"color" : colors,
    }
    return render(request, 'items.html', context)


