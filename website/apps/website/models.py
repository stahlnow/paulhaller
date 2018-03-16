from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.timezone import now

# from website.managers import PublicManager

from ckeditor.fields import RichTextField


class Post(models.Model):

    """Post model."""

    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='publish')
    author = models.ForeignKey(User)
    body = RichTextField(_('body'), )
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField(_('allow comments'), default=True)
    publish = models.DateTimeField(_('publish'), default=now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    # objects = PublicManager()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'website_posts'
        ordering = ('-publish',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'post_detail', (), {'slug': self.slug}

    # def get_previous_post(self):
    #     return self.get_previous_by_publish(status__gte=2)
    #
    # def get_next_post(self):
    #     return self.get_next_by_publish(status__gte=2)


class Poem(models.Model):

    """Poem model."""

    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='publish')
    author = models.ForeignKey(User)
    body = RichTextField(_('body'), )
    status = models.IntegerField(_('status'),choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField(_('allow comments'), default=True)
    publish = models.DateTimeField(_('publish'), default=now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    # objects = PublicManager()

    class Meta:
        verbose_name = _('poem')
        verbose_name_plural = _('poems')
        db_table = 'website_poems'
        ordering = ('-publish',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'poem_detail', (), {'slug': self.slug}

    # def get_previous_post(self):
    #     return self.get_previous_by_publish(status__gte=2)
    #
    # def get_next_post(self):
    #     return self.get_next_by_publish(status__gte=2)


class Letter(models.Model):

    """Letter model."""

    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='publish')
    author = models.ForeignKey(User)
    body = RichTextField(_('body'), )
    status = models.IntegerField(_('status'),choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField(_('allow comments'), default=True)
    publish = models.DateTimeField(_('publish'), default=now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    # objects = PublicManager()

    class Meta:
        verbose_name = _('letter')
        verbose_name_plural = _('letters')
        db_table = 'website_letters'
        ordering = ('-publish',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'letter_detail', (), {'slug': self.slug}

    # def get_previous_post(self):
    #     return self.get_previous_by_publish(status__gte=2)
    #
    # def get_next_post(self):
    #     return self.get_next_by_publish(status__gte=2)
