from django.db import models
from django.conf import settings
from apps.authentication.models import Role

class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    min_order_value = models.FloatField(null=False, default=0)
    delivery_fee = models.FloatField(null=False, default=0)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': Role.OWNER}
    )

    def __str__(self):
        return str(self.name)