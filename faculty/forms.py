# faculty/forms.py
from django import forms
from students.models import Marks

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'ia1', 'ia2', 'ia3', 'assignment1', 'assignment2', 'sub_code', 'cie_component']

