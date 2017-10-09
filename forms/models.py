from django.db import models
from datetime import datetime
from django import forms

# Create your models here.

class Question(models.Model):
    # 文字列のフィールド
    question_text = models.CharField(max_length=200)
    # 日時のフィールド
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Drilling(models.Model):
    drilling = models.BooleanField('drilling:')
    drilling_no = models.IntegerField('ｼｬﾝｸ部刻印No' ,default=0)
    drilling_exchange = models.BooleanField('drilling_exchange:')
    StartEnd = models.BooleanField('StartEnd:')
    Date = models.DateTimeField('日付選択',default= datetime.today())
    Time = models.DateTimeField('時間選択', default=datetime.now)
    first_diameter = models.IntegerField('刃先径', default=0)
    used_count = models.IntegerField('使用数', default=0)



