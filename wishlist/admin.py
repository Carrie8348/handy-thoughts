from django.contrib import admin
from .models import Wishlist

# Register your models here.
class  WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
    )


admin.site.register(Wishlist, WishlistAdmin)