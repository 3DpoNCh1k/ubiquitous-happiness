from django import forms
from .models import Question, Answer 

class AskForm(forms.Form):
    title = forms.CharField(max_length=1000)
    text = forms.CharField()
    # def clean(self):
        # pass
    def save(self):
        question = Question(title=self.cleaned_data["title"],
                            text=self.cleaned_data["text"])
        question.save()
        return question
    
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    
    def save(self):
        ans = Answer(question_id=self.question,
                    text=self.cleaned_data["text"])
        ans.save()
        return ans
