from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileModelForm
from . import views


def stock(request):
    import requests
    import json
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_2462f6f6db344a55b0a7cdc46b090cef")

    try:
        dolla = json.loads(api_request.content)


    except Exception as e:

        dolla = "Error..."


    return render(request, 'profiles/stock.html', {'dolla':dolla})


def panel(request):
    
    import requests
    import json
    #price data
    api_data = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETC,DOGE,LTC&tsyms=USD")
    data = json.loads(api_data.content)
    api_request = requests.get(
            "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    
    return render(request, 'profiles/home.html', { 'api':api, 'data':data})
# Create your views here.


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        quote_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(quote_request.content)        
        return render(request, 'profiles/prices.html', {'quote':quote,'crypto': crypto})

    else:
        notfound = "Enter a crypto symbol"
        return render(request, 'profiles/prices.html', {'notfound':notfound})


def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    form = ProfileModelForm(request.POST or None,
                            request.FILES or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.bio = form.cleaned_data.get('bio')
            instance.website = form.cleaned_data.get('website')
            instance.profile_picture = form.cleaned_data.get('profile_picture')
            form.save()

    context = {
        'object': profile,
        'form': form
    }

    return render(request, 'profiles/profile.html', context)

# def test_view(request):
#     hw = "Hello World"
#     return HttpResponse(hw)


# def test_view_1(request):
#     gs = "go to sleep"
#     return HttpResponse(gs)


# def test_view_2(request):
#     if request.user.is_authenticated:
#         user = request.user
#         profile = Profile.objects.get(user=user)
#     else:
#         profile = 'no profile'

#     context = {
#         'user': profile
#     }

#     return render(request, 'profiles/test.html', context)
