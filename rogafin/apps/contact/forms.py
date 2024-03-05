from django import forms

class ContactForm(forms.Form):  # Not forms.Forms
    name = forms.CharField(label='Name', max_length=100,)
    phoneNum = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email', max_length=100)
    credit_interest = forms.ChoiceField(label='¿QUÉ CREDITO ESTA INTERESADO?', choices=[
        ('opcion1', 'Adquisición de vivienda'),
        ('opcion2', 'Construcción'),
        ('opcion3', 'Terreno'),
        ('opcion4', 'Terreno + Construcción'),
        ('opcion5', 'Preventa'),
        ('opcion6', 'Liquidez'),
        ('opcion7', 'Automotriz'),
    ])
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'main_section3_container2_form_div_input'})
        self.fields['phoneNum'].widget.attrs.update({'class': 'main_section3_container2_form_div_input'})
        self.fields['email'].widget.attrs.update({'class': 'main_section3_container2_form_div_input'})
        self.fields['credit_interest'].widget.attrs.update({'class': 'main_section3_container2_form_div_input'})
        self.fields['message'].widget.attrs.update({'class': 'main_section3_container2_form_div_textarea'})

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
