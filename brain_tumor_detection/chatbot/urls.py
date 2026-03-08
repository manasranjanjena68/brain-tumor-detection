from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot_home'),
    path('ask/', views.ask_chatbot, name='ask_chatbot'),  # Correct view function
    path('history/', views.chatbot_history, name='chatbot_history'),  # Optional if you use history page
]
