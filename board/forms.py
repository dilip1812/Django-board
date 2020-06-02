from django import forms
from .models import Topic
from .models import Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}))
    solution = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}))
    class Meta:
        model = Topic
        fields = ['subject', 'message','solution']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]