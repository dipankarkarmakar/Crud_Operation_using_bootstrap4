from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import PersonForm
from .models import Person


@csrf_exempt
def person_list(request, template_name='person_list.html'):
    person = Person.objects.all()
    data = {}
    data['object_list'] = person
    return render(request, template_name, data)

@csrf_exempt
def person_view(request, pk, template_name='person_detail.html'):
    person= get_object_or_404(Person, pk=pk)
    return render(request, template_name, {'object':person})

@csrf_exempt
def person_create(request, template_name='person_form.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, template_name, {'form':form})

@csrf_exempt
def person_update(request, pk, template_name='person_form.html'):
    person= get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, template_name, {'form':form})

@csrf_exempt
def person_delete(request, pk, template_name='person_confirm_delete.html'):
    person= get_object_or_404(Person, pk=pk)
    if request.method=='POST':
        person.delete()
        return redirect('person_list')
    return render(request, template_name, {'object':person})