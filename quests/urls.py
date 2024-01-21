from django.urls import path
from quests import views


urlpatterns = [
    path('', views.quest_dashboard, name='quest_dashboard'),
    path('delete/<quest_id>', views.delete_quest, name='delete_quest'),
    path('edit/<quest_id>', views.edit_quest, name='edit_quest'),
    path('complete/<quest_id>', views.complete_quest, name='complete_quest'),
    path('pending/<quest_id>', views.pending_quest, name='pending_quest'),
]