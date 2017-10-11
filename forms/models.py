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
    drilling = models.CharField('drilling:', max_length=200)
    drilling_no = models.IntegerField('ｼｬﾝｸ部刻印No' ,default=0)
    drilling_exchange = models.CharField('drilling_exchange:', max_length=200)
    StartEnd = models.CharField('StartEnd:', max_length=200)
    Date = models.DateField('日付選択',default= datetime.today())
    Time = models.TimeField('時間選択', default=datetime.now)
    first_diameter = models.FloatField('刃先径', default=0)
    used_count = models.IntegerField('使用数', default=0)



