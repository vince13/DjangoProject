from django import forms

from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ["content"]
        widget = {
            "content": forms.Textarea(attrs={
                "class": "form-control"
            })
        }
