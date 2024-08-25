from django.forms import ModelForm

from .models import Post, PostAttachement

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ('body', 'is_private')
    

class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachement
        fields = ('image',)