from django import forms

class HandleForm(forms.Form):
	twitter_handle = forms.CharField(label='Twitter Handle', max_length=100)

class PushForm(forms.Form):
	push_source = forms.CharField(label='Source', max_length=16)
	push_handle = forms.CharField(label='Handle', max_length=100)