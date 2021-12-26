from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Rostov', 'Rostov'),
		('Chelybinsk', 'Chelybinsk'),
		('Ykaterinburg', 'Ykaterinburg '),
	)

	DISCRICT_CHOICES = (
		('VIZ', 'VIZ'),
		('Shartash', 'Shartash'),
		('Kirovskiy', 'Kirovskiy'),
	)

	PAYMENT_METHOD_CHOICES = (
		('MasterCard', 'MasterCard'),
		('Visa','Visa')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
