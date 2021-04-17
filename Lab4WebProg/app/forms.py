"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment,Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content','image',) # требуется заполнить только поле text
        labels = {'title': "Заголовок",'description':"Краткое содержание", 'content': "Полное содержание",'image':"Картинка"} # метка к полю формы text

class AnketaForm(forms.Form):
    name = forms.CharField(label="Ваше имя", min_length=2, max_length=100)
    city = forms.CharField(label="Ваш город", min_length=2, max_length=100)
    job = forms.CharField(label="Ваш род занятий", min_length=2, max_length=100)
    gender = forms.ChoiceField(
        label="Ваш пол",
        choices=[("1", "Муж"), ("2", "Жен")],
        widget=forms.RadioSelect,
        initial=1,
    )
    internet = forms.ChoiceField(
        label="Вы путешествуете",
        choices=(
            ("1", "Раз в год"),
            ("2", "Два раза в год"),
            ("3", "Раз в два года"),
            ("4", "Никогда"),
        ),
        initial=1,
    )
    notice = forms.BooleanField(label="Получать новости на e-mail?", required=False)
    email = forms.EmailField(label="Ваш e-mail", min_length=7)
    message = forms.CharField(
        label="Что хотели бы посетить?", widget=forms.Textarea(attrs={"rows": 10, "cols": 30})
    )

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

