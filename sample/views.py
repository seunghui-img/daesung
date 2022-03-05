from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sample/index.html')
def about(request):
    return render(request, 'sample/about.html')
def blog_home(request):
    return render(request, 'sample/blog-home.html')
def blog_post(request):
    return render(request, 'sample/blog-post.html')
def contact(request):
    return render(request, 'sample/contact.html')
def faq(request):
    return render(request, 'sample/faq.html')
def portfolio_item(request):
    return render(request, 'sample/portfolio-item.html')
def portfolio_overview(request):
    return render(request, 'sample/portfolio-overview.html')
def pricing(request):
    return render(request, 'sample/pricing.html')
    

def sample(request, name):
    if name == 'login':
        return render(request, 'sample/login.html')
    elif name == 'list':
        return render(request, 'sample/list.html')
    elif name == 'form':
        return render(request, 'sample/form.html')
    elif name == 'changelist':
        return render(request, 'sample/changelist.html')
    else:
        return render(request, 'sample/main.html')
