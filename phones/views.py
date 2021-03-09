from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
	template = 'catalog.html'
	sort_dict = {
		'name': 'name',
		'min_price': 'price',
		'max_price': '-price',
	}
	phones = Phone.objects.all()
	sort_key = request.GET.get('sort')
	if sort_key:
		if sort_key == 'min_price':
			phones = phones.order_by(sort_dict.get(sort_key, 'price'))
		elif sort_key == 'max_price':
			phones = phones.order_by(sort_dict.get(sort_key, '-price'))
		elif sort_key == 'name':
			phones = phones.order_by(sort_dict.get(sort_key, 'name'))
	else:
		phones = phones.order_by('name')
	return render(request, template, context={'phones': phones})


def show_product(request, slug):
	template = 'product.html'
	context = {'phone': Phone.objects.get(slug=slug)}
	return render(request, template, context)
