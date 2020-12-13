from django import forms
from .models import Question, Answer, User 

class AskForm(forms.Form):
    title = forms.CharField(max_length=1000)
    text = forms.CharField()
    _user=None
    # def clean(self):
        # pass
    def save(self):
        question = Question(title=self.cleaned_data["title"],
                            text=self.cleaned_data["text"],
                            author=self._user)
        question.save()
        return question
    
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    _user=None
    
    def save(self):
        print(dir(self))
        print(self.data)
        print(self.fields)
        print(self._user)
        ans = Answer(question_id=self.question,
                    text=self.cleaned_data["text"],
                    author=self._user)
        ans.save()
        return ans

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    
    def save(self):
        print(self.cleaned_data)
        me = User(username=self.cleaned_data["username"],
                  email=self.cleaned_data["email"],
                  password=self.cleaned_data["password"])
        me.set_password(me.password)
        me.save()
        return me


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
        
    def save(self):
        print(self.cleaned_data)
        return User.objects.get(username=username)
