from django import forms

from app.models import Event, Member,User,People,Contact
from app.authentication_form import AuthenticationForm
from django.core.mail import send_mail

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ()


class LoginForm(AuthenticationForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Bunday {email} allaqachon mavjud')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password did not match')

        return password


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    from_email = forms.EmailField()
    to = forms.EmailField()
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

""" class ContactForm(forms.Form):
    fullname = forms.CharField(label='Full Name', max_length=100)
    email_address = forms.EmailField(label='Email Address')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_email(self):
        # Assuming you have email credentials set up in settings.py
        send_mail(
            'Contact Form Submission',
            f'Name: {self.cleaned_data["fullname"]}\nEmail: {self.cleaned_data["email_address"]}\n\nMessage: {self.cleaned_data["message"]}',
            self.cleaned_data['sanjarbahodirov9901@gmail.com'], # Sender email
            ['farruxyoldoshov2409@gmail.com'], # Recipient email
            fail_silently=False,
        )
 """
class PeopleForm(forms.ModelForm):
   class Meta:
       model = People
       exclude =()