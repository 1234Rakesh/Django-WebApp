from django.shortcuts import render,redirect

from App_item.models import Category,Item

from .forms import SignupForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories':categories,
        'items':items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            
            return redirect('/login/')
        
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html',{
        'form':form
    })

# # from django.shortcuts import render, redirect
# # from django.urls import reverse  # Import the reverse function

# # from App_item.models import Category, Item
# # from .forms import SignupForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             # Use reverse to get the URL for the login page
#             login_url = reverse('/login/')  # Assuming the name of your login URL is 'login'
#             return redirect(login_url)
        
#     else:
#         form = SignupForm()
    
#     return render(request, 'core/signup.html', {'form': form})
