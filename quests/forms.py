from django import forms
from quests.models import Quest


class QuestForm(forms.ModelForm):

    class Meta:
        model = Quest
        fields = ['quest_name', 'status']