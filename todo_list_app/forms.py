from django import forms

from todo_list_app.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
