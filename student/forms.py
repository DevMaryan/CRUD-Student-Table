from django import forms
from student.models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('__all__')
        exclude = ['id','submitted']
        labels = {
            'name' : ('Student Name'),
            'surname' : ('Student Surname'),
            'age' : ('Student Age'),
            'email' : ('Student Email'),
        }