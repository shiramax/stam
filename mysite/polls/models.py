# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django import forms
from datetime import date




from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

#######################
#Quiz Structure Models#
#######################


class School(models.Model):
    school_name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.school_name


class Course(models.Model):
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.course_name


class Quiz(models.Model):

    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    date = models.DateField(null=True, blank=True)
    user_score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def possible(self):
        total = 0
        for question in self.question_set.all():
            question.save()
            total += question.value
        return total


class Tag(models.Model):
    content = models.CharField(max_length=50)
    vote = models.IntegerField(default=1)
    count_in_question = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    question_text = models.CharField(max_length=5000)


    def __unicode__(self):
        return self.question_text

    def get_correct_answer(self):
        for answer in self.answers:
            if answer.is_correct_answer:
                return answer.answer_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct_answer = models.BooleanField(True, name="is_correct_answer")
    user_choice = models.BooleanField(True, name="user_choice", default=False)

    def __unicode__(self):
        return self.answer_text



