# -*- coding: utf-8 -*-
from django import forms
from tinymce.widgets import TinyMCE

from blog.models import Comment, Post


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ("StudentName","StudentDOB","StudentAddress", "StudentAadhar","Score","School","SchoolAddress","FatherName","MotherName","GuardianPhoneNo","ParentOccupation",
        "ParentSalary","BPL","Total","BankDetails","thumbnail","category","featured")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
