from django import forms
from app.models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        q = Articles.objects.filter(title__icontains=title)
        if q:
            self.add_error('title', f'\"{title}\" is already taken')
        return data
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("Cleaned Data: ", cleaned_data)
    #     title = cleaned_data.get('title')
    #     print("Title: ", title)
    #     if title.lower().strip() == 'the office':
    #         raise forms.ValidationError('This title is already taken')
    #     return title

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     print("All Data: ", cleaned_data)
    #     title = cleaned_data.get('title')
    #     content = cleaned_data.get('content')
    #
    #     if "office" in title.lower():
    #         self.add_error('title', 'This title is already taken')
    #     elif "office" in content.lower():
    #         self.add_error('content', 'Office cannot be allowed in content')
    #     return cleaned_data