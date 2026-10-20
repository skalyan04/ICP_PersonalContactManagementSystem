from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContactForm
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all().order_by("name")
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


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
