from django.contrib import admin

from content.models import About, Blog, Contact, Portfolio, PrimarySkill, Profile, SecondarySkill, Service, Testimonial

# Register your models here.
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(PrimarySkill)
admin.site.register(SecondarySkill)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Contact)
