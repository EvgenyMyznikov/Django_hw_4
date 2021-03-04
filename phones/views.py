from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
	template = 'catalog.html'
	sort = request.GET.get('sort')
	if sort:
		if sort == 'name':
			context = {'phones': Phone.objects.order_by('name').all()}
			return render(request, template, context)
		elif sort == 'min_price':
			context = {'phones': Phone.objects.order_by('price').all()}
			return render(request, template, context)
		elif sort == 'max_price':
			context = {'phones': Phone.objects.order_by('-price').all()}
			return render(request, template, context)
	else:
		return render(request, template, context={
			'phones': Phone.objects.all()
		})


def show_product(request, slug):
	template = 'product.html'
	context = {'phone': Phone.objects.get(slug=slug)}
	return render(request, template, context)
