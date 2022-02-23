from django import forms
from django.forms import ModelForm
from owner.models import Books,Employee
class BookForm(ModelForm):
    class Meta:
        model=Books
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={'class':'form-control'}),
            "author":forms.TextInput(attrs={'class':'form-control'}),
            "price":forms.NumberInput(attrs={'class':'form-control'}),
            "copies":forms.NumberInput(attrs={'class':'form-control'}),
            "published_date":forms.DateInput(attrs={'class':'form-control','type':'date'}),
            # "image":forms.FileInput(attrs={'class':'form-control'})
        }
class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        widgets={
            "employee_name":forms.TextInput(attrs={"class":"form-control"}),
            "employee_desig":forms.TextInput(attrs={"class":"form-control"}),
            "employee_exp":forms.NumberInput(attrs={"class":"form-control"}),
            "employee_salary":forms.NumberInput(attrs={"class":"form-control"}),
        }
    # book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # price=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    # copies=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    # def clean(self):
    #     cleaned_data=super().clean()
    #     price=cleaned_data.get('price')
    #     if price<0:
    #         msg="Invalid Price"
    #         self.add_error('price',msg)
    #     copies=cleaned_data.get('copies')
    #     if copies<0:
    #         msg="Invalid Number of Copies"
    #         self.add_error('copies',msg)