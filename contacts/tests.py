from django.test import TestCase
from django.urls import reverse

from .models import Contact


class ContactPhoneValidationTests(TestCase):
    def test_add_contact_requires_phone_number(self):
        response = self.client.post(
            reverse("add_contact"),
            {"name": "Test Contact", "phone": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a phone number.")
        self.assertFalse(Contact.objects.exists())

    def test_edit_contact_cannot_remove_phone_number(self):
        contact = Contact.objects.create(name="Test Contact", phone="1234567890")

        response = self.client.post(
            reverse("edit_contact", args=[contact.pk]),
            {"name": contact.name, "phone": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a phone number.")
        contact.refresh_from_db()
        self.assertEqual(contact.phone, "1234567890")
