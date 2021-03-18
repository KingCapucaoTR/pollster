from django.db import models

# Create your models here.

#Question model\table
class Question(models.Model):
    #fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #display the question_text
    def __str__(self):
        return self.question_text

#Choice model\table
class Choice(models.Model):
    #PK to FK relationship -- on_delete means if something is deleted from Question the related Choices will be deleted as well
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #display the choice_text
    def __str__(self):
        return self.choice_text

