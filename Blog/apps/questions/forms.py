from .views import Question,Answer
from django.forms import Form,ModelForm

class QuestionCreateForm(ModelForm):
    class Meta:
        model = Question
        fields = ('title','body',)


class AnswerCreateForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)