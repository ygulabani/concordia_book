from django.urls import path
from .views import home, textbook_list

urlpatterns = [
    path('', home, name='home'),  # 👈 New homepage route
    path('textbooks/<str:course_code>/', textbook_list, name='textbook_list'),
]
