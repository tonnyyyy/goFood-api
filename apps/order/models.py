from re import L
from django.db import models
from apps.restaurant.models import Restaurant
from apps.authentication.models import Role
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        limit_choices_to={'role': Role.CUSTOMER}
    )
    order_date = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateTimeField(blank=True, null=True)

    @property
    def order_items(self):
        return self.orderitem_set.all()

    @property
    def order_items_quantity(self):
        return len(self.orderitem_set.all())

    def __str__(self):
        return f'{self.customer} | {self.order_date.strftime("%Y-%m-%d at %H:%M")} | {len(self.order_items)} items'


class Menu(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    @property
    def food_items(self):
        return self.fooditem_set.all()

    def __str__(self):
        return f'{self.id} - from {self.restaurant}'

    @property
    def changeform_link(self):
        if self.id:
            changeform_url = reverse(
                'admin:order_menu_change', args=(self.id,)
            )
            return mark_safe(u'<a href="%s" target="_blank">Details</a>' % changeform_url)
        return u''
    
    changeform_link.fget.short_description = ''



class FoodItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField()

    def __str__(self):
        return f'{self.name}{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(blank=True)
    unit_price = models.FloatField(blank=True)

    def __str__(self):
        return f'{self.id} | {self.food}'

    def save(self, *args, **kwargs):
        # quando criar um OrderItem e não for informado a quantidade ou preço,
        # atribuir os valores da foreignKey em self.food
        if (not self.id):
            self.quantity = self.food.quantity if (not self.quantity) else self.quantity
            self.unit_price = self.food.unit_price if (not self.unit_price) else self.unit_price

        super(OrderItem, self).save()
