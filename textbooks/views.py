from django.shortcuts import render
from .models import Textbook

def textbook_list(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)

    return render(request, 'textbooks/textbook_list.html', {
        'textbooks': textbooks,
        'course_code': course_code
    })

def home(request):
    return render(request, 'textbooks/home.html')
