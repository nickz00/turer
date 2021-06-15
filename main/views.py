from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import clients, interested, advertising
from .forms import add_client, add_interested,add_adver


def index(request):
    return render(request, 'main/index.html')


def client(request):
    context = {'data': clients.objects.all()}
    return render(request, 'main/client.html', context=context)


@csrf_exempt
def client_add(request):
    if request.method == 'POST':
        form = add_client(request.POST)
        if form.is_valid():
            print('qwrtqwt')
            clients(**form.cleaned_data).save()
            return HttpResponseRedirect('/client')
    else:
        context = {'form': add_client()}
        return render(request, 'main/add_client.html', context=context)


def client_delite(request, c_id):
    clients.objects.get(id=c_id).delete()
    return HttpResponseRedirect('/client')


def one_client(request, c_id):
    context = {'data': clients.objects.get(id=c_id)}
    return render(request, 'main/one_client.html', context=context)


@csrf_exempt
def one_client_change(request, c_id):
    if request.method == 'POST':
        form = add_client(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            clients(**form.cleaned_data).save()
            clients.objects.get(id=c_id).delete()
            return HttpResponseRedirect('/client')
    else:
        context = {'data': clients.objects.get(id=c_id)}
        return render(request, 'main/change_client.html', context=context)


@csrf_exempt
def client_change(request, c_id):
    if request.method == 'POST':
        form = add_client(request.POST)
        if form.is_valid():
            print('qwrtqwt')
            clients(**form.cleaned_data).save()
            return HttpResponseRedirect('/client')
    else:
        context = {'form': add_client()}
        return render(request, 'main/change_client.html', context=context)


# ----------------------------------------------------------------------------------


def interested_(request):
    context = {'data': interested.objects.all()}
    return render(request, 'main/interested.html', context=context)


@csrf_exempt
def interested_add(request):
    if request.method == 'POST':
        form = add_interested(request.POST)
        if form.is_valid():
            interested(**form.cleaned_data).save()
            return HttpResponseRedirect('/interested')
    else:
        context = {'form': add_interested()}
        return render(request, 'main/add_interested.html', context=context)


def interested_delite(request, i_id):
    interested.objects.get(id=i_id).delete()
    return HttpResponseRedirect('/interested')


def one_interested(request, i_id):
    context = {'data': interested.objects.get(id=i_id)}
    return render(request, 'main/one_interested.html', context=context)


@csrf_exempt
def one_interested_change(request, i_id):
    if request.method == 'POST':
        form = add_interested(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            interested(**form.cleaned_data).save()
            interested.objects.get(id=i_id).delete()
            return HttpResponseRedirect('/interested')
    else:
        context = {'data': interested.objects.get(id=i_id)}
        return render(request, 'main/change_interested.html', context=context)


# ------------------------------------------------------------------------


def all_advertising(request):
    context = {'data': advertising.objects.all()}
    return render(request, 'main/all_advertising.html', context=context)

@csrf_exempt
def add_advertising(request):
    if request.method == 'POST':
        form = add_adver(request.POST)
        if form.is_valid():
            advertising(**form.cleaned_data).save()
            return HttpResponseRedirect('/all_advertising')
    else:
        context = {'form':add_adver()}
        return render(request, 'main/add_advertising.html', context=context)

