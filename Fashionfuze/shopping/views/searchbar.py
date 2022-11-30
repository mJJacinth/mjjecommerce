from django.shortcuts import render , redirect , HttpResponseRedirect
from shopping.models.product import Products
from shopping.models.category import Category
from django.views import View


# Create your views here.
class searchbar(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')





def searchbar(request):
        searchedproduct=request.GET['searchcourse']
        products=Products.objects.filter(description__icontains=searchedproduct)
        categories = Category.get_all_categories()
        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'index.html',data)
