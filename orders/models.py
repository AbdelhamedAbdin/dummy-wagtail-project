from django.db import models
from django.utils import timezone
from wagtail.admin.panels import FieldPanel

from wagtail.models import Page

from products.models import ProductsPage


class OrdersPage(Page):
    date_created = models.DateTimeField(default=timezone.now)

    content_panels = Page.content_panels + [
        FieldPanel('date_created'),
    ]


class OrderItem(Page):
    product = models.ForeignKey(
        ProductsPage,
        on_delete=models.SET_NULL,
        null=True
    )
    order = models.ForeignKey(
        OrdersPage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    quantity = models.PositiveIntegerField(default=0)

    content_panels = Page.content_panels + [
        FieldPanel('product'),
        FieldPanel('order'),
        FieldPanel('quantity')
    ]
