from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
# Create your views here.


def all_chai(request):
    # Fetch all chai varities from the database and pass to the template
    chais = ChaiVarity.objects.all() # this come from list formate
    for chai in chais:
        print(f"chai id is : {chai.id}")
        print(f"chai name is : {chai.name}")
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})


def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVerityForm(request.POST)
        if form.is_valid():
            selected_chai = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varities = selected_chai)
    else:
        form = ChaiVerityForm()
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})