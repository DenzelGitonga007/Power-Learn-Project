# Import forms from django
from django import forms

# Copied from: https://docs.google.com/document/d/1f1-1YmoOW6630YutaqhImedBmwubRFAXLxTyOgzOUBM/edit

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (
('Manager', 'Manager'),
('Cashier', 'Cashier'),
('Operator', 'Operator')
) 
    field = forms.ChoiceField(choices=posts)
