from django import forms

class ContactForm(forms.Form):
    adresse_email= forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={'placeholder': 'Adresse Email Utilisateur'}))
    objet = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':10, 'cols':100, 'placeholder': 'Preciser en quelques mots la nature des donnees souhaitees'}))
