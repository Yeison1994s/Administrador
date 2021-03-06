from django import forms
from django.contrib.auth.models import User
from .models import Client,SocialNetwork

#Const
ERROR_MESSAGE_USER = {'required': 'El username es nesesario',
'unique':'El username ya se encuentra registrado','invalid':'Ingrese un username valido'}
ERROR_MESSAGE_PASSWORD = {'required':'El password es necesario'}
ERROR_MESSAGE_EMAIL = {'required': 'El username es nesesario',
'invalid':'Ingrese un correo valido'}

#Functions
def password_validation(value_password):
	if len(value_password) < 5:
		raise forms.ValidationError('The password requires minimun 5 characters')

#Class
class LoginUserForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput())

	def __init__(self, *args, **kwargs):
	    super(LoginUserForm, self).__init__(*args, **kwargs)
	    self.fields['username'].widget.attrs.update({'id':'username_login','class':'input_login'})
	    self.fields['password'].widget.attrs.update({'id':'username_login','class':'input_login'})
class CreateUserForm(forms.ModelForm):
	username = forms.CharField(max_length=30, error_messages=ERROR_MESSAGE_USER)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput(),error_messages=ERROR_MESSAGE_PASSWORD)
	email = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL)

	def __init__(self, *args, **kwargs):
	    super(CreateUserForm, self).__init__(*args, **kwargs)
	    self.fields['username'].widget.attrs.update({'id':'username_create'})
	    self.fields['password'].widget.attrs.update({'id':'password_login'})
	    self.fields['email'].widget.attrs.update({'id':'email_create'})

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).count():
			raise forms.ValidationError('El email debe de ser unico.')
		return email


	class Meta:
		model= User
		fields =('username','password','email')
class EditUserForm(forms.ModelForm):
	username = forms.CharField(max_length=30, error_messages=ERROR_MESSAGE_USER)
	email = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL)
	first_name = forms.CharField(label='Nombre')
	last_name = forms.CharField(label='Apellido')
	class Meta:
		model = User
		fields =('username','email','first_name','last_name')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exclude(pk=self.instance.id).count():
			raise forms.ValidationError('El email debe de ser unico.')
		return email
class EditPasswordForm(forms.Form):
	password = forms.CharField(label='Contraseña actual', max_length=20, widget=forms.PasswordInput())
	new_password = forms.CharField(label='Nueva contraseña', max_length=20, widget=forms.PasswordInput(),validators=[password_validation])
	repeat_password = forms.CharField(label='Repetir nueva contraseña',max_length=20, widget=forms.PasswordInput(),validators=[password_validation])

	def clean(self):
		clean_data = super(EditPasswordForm,self).clean()
		password1 = clean_data['new_password']
		password2 = clean_data['repeat_password']
		if password1 != password2:
			raise forms.ValidationError('los passwords no coinciden')
class EditClientForm(forms.ModelForm):
	job = forms.CharField(label='Trabajo actual',required=False)
	bio = forms.CharField(label='Biografía', widget=forms.Textarea,required=False)

	class Meta:
		model = Client
		exclude = ['user1']

		def __init__(self, *args, **kwargs):
			super(EditClientForm, self).__init__(*args, **kwargs)
			self.fields['job'].widget.attrs.update({'id':'job_edit_client','class':'validate'})
			self.fields['bio'].widget.attrs.update({'id':'bio_edit_client','class':'validate'})

class EditSocialForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        exclude = ['user']


    
			



