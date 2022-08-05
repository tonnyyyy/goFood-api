from functools import wraps
from types import FunctionType

from django.contrib import admin
from django import forms
from django.forms import BaseInlineFormSet
from apps.restaurant.models import Restaurant
from apps.order.models import FoodItem, Menu


# class MenuForm(forms.ModelForm):

#     class Meta:
#         model = Menu
#         fields = ('changeform_link',)

#     changeform_link = forms.CharField(max_length=255)

#     def __init__(self, *args, **kwargs):
#         instance = kwargs.get('instance', None)
#         if instance:
#             kwargs['initial'] = {'changeform_link': instance.changeform_link }
#         super().__init__(*args, **kwargs)

#     def save(self, *args, **kwargs):
#         self.instance.changeform_link = str(args)
#         return super().save(*args, **kwargs)

class FoodItemInline(admin.TabularInline):
    model = FoodItem

class MenuInline(admin.StackedInline):
    model = Menu
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [MenuInline]

