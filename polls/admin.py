from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ["pub_date"]
    search_fields = ["txtQuestion"]
        
    fieldsets = [
        (None, {'fields': ['txtQuestion']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    
    inlines = [ChoiceInLine]
    


admin.site.register(Question, QuestionAdmin)
