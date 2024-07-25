from django import forms
import datetime
from .models import Post,Comment

class postcreate(forms.ModelForm):
    published_date=forms.DateField(label='published_date', widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    class Meta:
        model=Post
        fields=['title','content','published_date']
    

class postedit(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']


class AddComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']