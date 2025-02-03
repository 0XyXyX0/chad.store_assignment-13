from django.contrib import admin
from categories.models import Category, CategoryImage


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryImageInline]


admin.site.register(CategoryImage)
