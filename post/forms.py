from django import forms

from post.models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = "__all__"