from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField

from wagtail.models import Page
from wagtail.api import APIField


class TestApp(Page):
    test_field = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('test_field')
    ]
