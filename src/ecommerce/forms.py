from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu Nome Completo"}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu Email"}))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Sua Mensagem"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email tem que ser gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome', widget=forms.TextInput(attrs={"placeholder": "Nome"}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={"placeholder": "Senha"}))

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nome', widget=forms.TextInput(attrs={"placeholder": "Nome"}))
    email = forms.EmailField()
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={"placeholder": "Senha"}))
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput(attrs={"placeholder": "Confirme a Senha"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Usuário já existe")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email já existe")
        return email

    def clean(self):
        data = self.cleaned_data
        pasasword = self.cleaned_data.get("password")
        pasasword2 = self.cleaned_data.get("password2")
        if pasasword2 != pasasword:
            raise forms.ValidationError("Senhas não conferem")
        return data