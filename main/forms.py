from news.models import novost  # или novost, если у тебя с маленькой буквы
from django.forms import ModelForm, TextInput, DateInput, Textarea

class novostForm(ModelForm):
    class Meta:
        model = novost
        fields=['title','intro', 'text', 'date', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название статьи"
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс статьи"
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата публикации"
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст статьи"
            }),
            


        }

    