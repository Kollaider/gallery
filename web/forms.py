from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(required=False, label='New comment', max_length=100)

    def clean_comment(self):
        data  = self.cleaned_data['comment']
        return data