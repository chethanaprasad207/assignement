class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'