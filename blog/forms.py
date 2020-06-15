from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        comment = Comment(**self.cleaned_data)
        comment.set_password(comment.password)
        self.instance = comment
        if commit:
            self.instance.save()
        return self.instance
