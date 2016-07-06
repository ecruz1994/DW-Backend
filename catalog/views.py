from django.shortcuts import render

def view_index(request):
	pass

def category(request,category_id):

	products = Product.objects.filter(category__id=category_id)

	return render(request, 'category.html', {'products':products})

def post_list(request):
        return render(request, 'post_list.html', {})