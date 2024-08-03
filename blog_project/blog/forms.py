from django import forms
import datetime
from .models import Post

class postcreate(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
    

class postedit(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
