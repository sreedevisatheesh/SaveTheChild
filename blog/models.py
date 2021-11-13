# -*- coding: utf-8 -*-
from io import BytesIO
import django.utils.timezone as dt
from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField
from datetime import date
from accounts.models import Author


class Category(models.Model):
    id=models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    )
    StudentName = models.CharField(_("Student Name"), max_length=50,default="")

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.StudentName


class Post(models.Model):

    
    StudentName=models.CharField(_("Student Name"), max_length=100)
    StudentDOB=models.DateField(verbose_name= "Student Date of Birth",default=dt.now)
   
    StudentAddress=models.TextField(_("Student Address"),max_length=300)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    StudentAadhar= models.IntegerField(max_length=12, verbose_name="Student Aadhar Number")
    School=models.TextField(max_length=100,verbose_name=" Class and School Name")
    SchoolAddress=models.TextField(max_length=300,verbose_name="Enter School Address")
    Score= models.IntegerField(max_length=3, verbose_name="Score Of Previous Year out of 100")
    FatherName= models.CharField(max_length=100, verbose_name="Father Name")
    MotherName=models.CharField(max_length=100, verbose_name="Mother Name")
    GuardianPhoneNo=models.IntegerField(max_length=10,verbose_name="Guardian Phone Number")
    ParentOccupation= models.CharField(max_length=100, verbose_name="Parent/Guardian Occupation",default="")
    ParentSalary= models.IntegerField(max_length=100, verbose_name="Parent/Guardian Salary per annum",default=0)
    BPL= models.TextField(max_length=12, verbose_name="Enter BPL card number")
    
    Total=models.IntegerField("Enter the total estimated amount")
    BankDetails=models.TextField(verbose_name=("Enter the bank details of school(Account Number,IFSC code,Branch)"))
    featured = models.BooleanField(_("Update if Sponsored"), default=False)          
    
                
    thumbnail=models.ImageField(
                        blank=True,
                        default="testing.jpeg",
                        upload_to="thumbnail",
                        verbose_name="Upload Student Image",
                    )

    category = models.ManyToManyField(
        Category, verbose_name=_("Category"), related_name="post"
    )
    author = models.ForeignKey(
        Author, verbose_name=_("Author"), on_delete=models.CASCADE
    )
   
    
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.StudentName

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        """Update URL for Post"""
        return reverse("update_applicant", kwargs={"slug": self.slug})

    def get_delete_url(self):
        """Delete URL for Post"""
        return reverse("delete_applicant", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.StudentName)
        super().save(*args, **kwargs)
        if self.thumbnail:
            img = Image.open(default_storage.open(self.thumbnail.name))
            if img.height > 1080 or img.width > 1920:  # pragma:no cover
                output_size = (1920, 1080)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.thumbnail.name, buffer)


class Comment(models.Model):
 
    content=models.ImageField(
                        blank=True,
                        default="testing.jpeg",
                        upload_to="thumbnail",
                        verbose_name="Upload Student Progress Report",
                    )

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.user.user.username


class Newsletter(models.Model):

    email = models.EmailField(_("Email"), max_length=254)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)

    class Meta:
        verbose_name = _("newsletter")
        verbose_name_plural = _("newsletters")

    def __str__(self):
        return self.email
