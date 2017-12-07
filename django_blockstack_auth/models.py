# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class UserPrivateKey(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blockstack_keys',
        on_delete=models.CASCADE
    )

    key = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.key


class UserPublicKey(models.Model):
    private_key = models.ForeignKey(
        UserPrivateKey,
        related_name='public_keys'
    )

    key = models.CharField(max_length=128, db_index=True)

    def __unicode__(self):
        return self.key

    class Meta:
        unique_together = ('key', 'private_key')
