# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class UserPublicKey(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='public_keys',
        on_delete=models.CASCADE
    )

    key = models.CharField(max_length=128, db_index=True)

    def __unicode__(self):
        return self.key

    class Meta:
        unique_together = ('key', 'user')
