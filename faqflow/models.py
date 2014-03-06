from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth import get_user_model


class Comment(models.Model):

    body = models.TextField(_('body'))
    attachment = models.FileField(_('attachment'), null=True, blank=True, upload_to='faqflow_attachments')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    changed_at = models.DateTimeField(_('changed at'), auto_now=True)
    author = models.ForeignKey(get_user_model(), verbose_name=_('author'), editable=False)

    class Meta:
        abstract = True


class Question(Comment):

    title = models.CharField(_('question'), max_length=255)
    notify = models.BooleanField(_('send me an e-mail when answers are posted'), default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')


class Answer(Comment):

    parent = models.ForeignKey(Question, verbose_name=_('parent'), editable=False)

    def __unicode__(self):
        return self.body[:50] + '...'

    class Meta:
        verbose_name = _('answer')
        verbose_name_plural = _('answers')