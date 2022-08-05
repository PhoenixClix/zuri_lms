from django.db import models

# Create your models here.

class Question(models.Model):
    # id = models.PrimaryKey(auto_increment=True)
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)


# 1)  "Are you happy about Django"         "June 16, 09:50 WAT"
# 2)  "Are you ..."                        "June 17, 10:00 WAT"


class Choices(models.Model):
    # number of choices
    # link to a Question
    # choice of answer    [Yes/No]
    # votes
    # id=models.PrimaryKey(auto_increment=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    vote = models.IntegerField(default=0)


    # 1)  "Are you happy about Django"        yes/no     3/0