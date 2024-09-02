from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField

from wagtail.models import Page
from wagtail.api import APIField


class ProductsPage(Page):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        FieldPanel('product_name'),
        FieldPanel('product_price'),
        PageChooserPanel('product_image')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        get_live_products = self.get_children().live()
        context['live_products'] = get_live_products
        return context

    def product_image_thumb(self):
        if self.product_image:
            return self.product_image.get_rendition('fill-100x100').img_tag()
        return "No Image"

    product_image_thumb.short_description = "Image"
    product_image_thumb.allow_tags = True
