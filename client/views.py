from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddClientForm
from .models import Client

@login_required
def clients_list(request):
  clients = Client.objects.filter(created_by=request.user)
  return render(request, 'client/clients_list.html', {'clients': clients})

@login_required
def clients_detail(request, pk):
  client = get_object_or_404(Client, created_by=request.user, pk=pk)
  
  return render(request, 'client/clients_detail.html', {
    'client': client
    })

@login_required
def clients_add(request):
  if request.method == 'POST':
    form = AddClientForm(request.POST)
    
    if form.is_valid():
      client = form.save(commit=False)
      client.created_by = request.user
      client.save()
    
      messages.success(request, 'O cliente foi criado com sucesso!')
      
      return redirect('clients_list')
    else:
      form = AddClientForm()

  return render(request, "client/clients_add.html", {
    'form': form
  })

@login_required
def clients_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()
    
    messages.success(request, 'O item foi deletado com sucesso!')
    
    return redirect('clients_list')

@login_required
def clients_edit(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
      form = AddClientForm(request.POST, instance=client)

      if form.is_valid():
        form.save()
        
        messages.success(request, 'Editado com sucesso!')

        return redirect('clients_list')
    else:
      form = AddClientForm(instance=client)

    return render(request, "client/clients_edit.html", {
      'form': form
    })
