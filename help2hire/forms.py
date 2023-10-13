from django import forms
from .models import Eventlist, JobApplication

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Eventlist
        fields = '__all__'
        

        


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['application_text']
        labels = {'application_text': 'Cover Letter'}
        widgets = {
            'application_text': forms.Textarea(attrs={'rows': 5}),
        }

        
'''class JobApplicationForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    cover_letter = forms.CharField(widget=forms.Textarea, label='Cover Letter')'''

   

