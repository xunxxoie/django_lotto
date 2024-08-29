from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
    class Meta:
        model = GuessNumbers
        fields = ('name','text') # form을 통해 입력받을 데이터의 변수명