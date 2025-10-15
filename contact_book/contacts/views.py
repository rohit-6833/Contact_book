from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Contact
from .forms import ContactForm, ContactSearchForm

def contact_list(request):
    """Display list of contacts with search functionality"""
    contacts = Contact.objects.all()
    
    # Handle search
    search_form = ContactSearchForm(request.GET)
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        if search_query:
            contacts = contacts.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone_number__icontains=search_query)
            )
    
    # Pagination
    paginator = Paginator(contacts, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    
    context = {
        'contacts': contacts,
        'search_form': search_form,
    }
    return render(request, 'contacts/contact_list.html', context)

def contact_detail(request, pk):
    """Display contact details"""
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

def contact_create(request):
    """Create a new contact"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f'Contact "{contact.full_name}" created successfully!')
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': 'Add New Contact',
        'button_text': 'Create Contact'
    })

def contact_update(request, pk):
    """Update an existing contact"""
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f'Contact "{contact.full_name}" updated successfully!')
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': f'Edit {contact.full_name}',
        'button_text': 'Update Contact'
    })

def contact_delete(request, pk):
    """Delete a contact"""
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        contact_name = contact.full_name
        contact.delete()
        messages.success(request, f'Contact "{contact_name}" deleted successfully!')
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
