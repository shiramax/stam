from django.contrib import admin
from .models import School, Course, Quiz, Tag,  Question, Answer

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)

