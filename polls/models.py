from django.db import models

# Create your models here.

class Question(models.Model):
    # id = models.PrimaryKey(auto_increment=True)
    question_text = models.CharField(max_length=255)
    question_description = models.CharField(max_length=255, default="Basic Description")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
    
# 1)  "Are you happy about Django"         "June 16, 09:50 WAT"
# 2)  "Are you ..."                        "June 17, 10:00 WAT"

# Create Table question(
#     question_text str;
#     pub_date date;
# )


class Choices(models.Model):
    # number of choices
    # link to a Question
    # choice of answer    [Yes/No]
    # votes
    # id=models.PrimaryKey(auto_increment=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} ---> {self.choice_answer}"


    # 1)  "Are you happy about Django"        yes/no     3/0