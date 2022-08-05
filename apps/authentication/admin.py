from django.contrib import admin
from apps.authentication.models import Role, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.restaurant.models import Restaurant

class RestaurantInline(admin.StackedInline):
    model = Restaurant
    fields = ('name', 'min_order_value', 'delivery_fee')

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'full_name', 'role')
    list_display_links = ('username', 'full_name')
    list_editable = ('role',)
    list_filter = ('is_superuser', 'role')
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    inlines = []
    # só exibe os restaurantes do usuário, se ele a 'role' dele for OWNER
    def get_inline_instances(self, request, obj):
        if (obj.role_id is Role.OWNER):
            self.inlines = [RestaurantInline]
            return super().get_inline_instances(request, obj)
        else:
            return []


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass