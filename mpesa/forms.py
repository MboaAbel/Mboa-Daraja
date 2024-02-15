from django import forms


class PaymentForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', help_text="Phone Number where Mpesa Notification is sent.")
    amount = forms.CharField(label='Payment Amount', help_text="Amount of  money in KES .")
    account_reference = forms.CharField()
    transaction_desc = forms.CharField()
    occassion = forms.CharField()
    checkoutRequestID = forms.CharField()
    timestamp = forms.NumberInput()