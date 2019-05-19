from django.shortcuts import render, redirect
from .models import inserting


def index(request):
	data = inserting.objects.all()
	return render(request, 'index.html', {'data':data})


def create(request):
	print(request.POST)
	name = request.GET['name']
	fname = request.GET['fname']
	mname = request.GET['mname']
	age = request.GET['age']
	raj = inserting(name=name, fname=fname, mname=mname, age=age)
	raj.save()
	return redirect('/')


def delete(request, id):
	data = inserting.objects.get(pk=id)
	data.delete()
	return redirect('/')


def edit(request, id):
	data = inserting.objects.get(pk=id)
	contain = {'data':data}

	return render(request, 'edit.html', {'data': data})

def update(request,id):
	data = inserting.objects.get(pk=id)
	data.name = request.GET['name']
	data.fname = request.GET['fname']
	data.mname = request.GET['mname']
	data.age = request.GET['age']
	data.save()
	return redirect('/')