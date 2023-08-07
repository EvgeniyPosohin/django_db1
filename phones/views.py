from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', None)
    types = {"name": Phone.objects.all().order_by('name'),
             "max_price": reversed(Phone.objects.all().order_by('price')),
             'min_price': Phone.objects.all().order_by('price'),
             None: Phone.objects.all(),
             }
    context = {"phones": types[sort]}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
