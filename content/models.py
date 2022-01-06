from django.db import models
from django.urls import reverse
# Create your models here.
# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to="profile/")
    full_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    bio = models.TextField()
    cv = models.FileField(upload_to="profile/cv")

    

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
        get_latest_by = ['full_name']

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class About(models.Model):
    long_about = models.TextField()
    short_about = models.TextField()

    

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Abouts")

    def __str__(self):
        return self.short_about

    # def get_absolute_url(self):
    #     return reverse("About_detail", kwargs={"pk": self.pk})

class PrimarySkill(models.Model):
    icon = models.ImageField(upload_to="Primaryskill/")
    name = models.CharField(max_length=50)

    

    class Meta:
        verbose_name = ("PrimarySkill")
        verbose_name_plural = ("PrimarySkills")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("PrimarySkill_detail", kwargs={"pk": self.pk})

class SecondarySkill(models.Model):
    icon = models.ImageField(upload_to="Secondaryskill/")
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("SecondarySkill")
        verbose_name_plural = ("SecondarySkills")

    def __str__(self):
        return self.name

class Service(models.Model):
    link = models.CharField(max_length=150)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Service_detail", kwargs={"pk": self.pk})

class Portfolio(models.Model):
    link = models.CharField(max_length=150)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Portfolio")
        verbose_name_plural = ("Portfolios")

    def __str__(self):
        return self.name

class Blog(models.Model):
    link = models.CharField(max_length=150)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    image = models.ImageField( upload_to="testimonial/client")
    image_name = models.CharField(max_length=50)
    fullname = models.CharField( max_length=50)
    designation = models.CharField(max_length=50)
    quote = models.TextField()

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.fullname


