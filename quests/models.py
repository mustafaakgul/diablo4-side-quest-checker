from django.db import models
from django.contrib.auth.models import User
from core.models import Base


class Quest(Base):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quest_name = models.CharField(max_length=300)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.quest_name + " - " + str(self.status)

    class Meta:
        ordering = ["status"]