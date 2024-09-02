from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import ProductsPage


class ProductAdmin(ModelAdmin):
    model = ProductsPage
    base_url_path = "productadmin"  # customise the URL from default to admin/bookadmin
    menu_label = "Product"  # ditch this to use verbose_name_plural from model
    # menu_icon = "pilcrow"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ("title", "product_name", "product_price", "product_image_thumb")
    list_filter = ("title",)
    search_fields = ("title", "product_name", "product_price")


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(ProductAdmin)



from wagtail import hooks

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return """
    <link rel="stylesheet" href="/static/css/admin-custom.css">
    """

@hooks.register('insert_global_admin_js')
def global_admin_js():
    return """
    <script src="/static/js/admin-custom.js"></script>
    """
