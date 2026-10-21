from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .forms import ContactForm
from .models import Contact


def contact_list(request):
    search_query = request.GET.get("q", "").strip()
    contacts = Contact.objects.all()

    if search_query:
        contacts = contacts.filter(
            Q(name__icontains=search_query) | Q(phone__icontains=search_query)
        )

    contacts = contacts.order_by("name")
    return render(request, "contacts/contact_list.html", {
        "contacts": contacts,
        "search_query": search_query,
    })


def add_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_list")
    return render(request, "contacts/contact_form.html", {
        "form": form,
        "title": "Add Contact",
    })


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_list")
    return render(request, "contacts/contact_form.html", {
        "form": form,
        "title": "Edit Contact",
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contacts/contact_confirm_delete.html", {
        "contact": contact,
    })
