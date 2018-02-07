from django import forms

from .models import complain

category_list = [
	('Carpenter','Carpenter'),
	('Electrician','Electrician'),
	('Plumber','Plumber'),
	('Others','Others')
]
class complainForm(forms.ModelForm):
	tag = forms.CharField(widget=forms.Select(choices=category_list, attrs={'class':'form-control'}), label="Tag")

	class Meta:
		model = complain
		fields = ['myname','enrollment','room','mobile','date_of_register','problem','tag' ]
