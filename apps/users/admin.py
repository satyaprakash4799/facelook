"""Django Admin View configuration."""
from django.contrib import admin
from .models import UserProfile, UserProfileInfo


class UserProfileAdmin(admin.ModelAdmin):
    """Customising admin view of UserProfile class."""

    '''Displaying all the fields in admin in order.'''
    # fields = ['user', 'name', 'email']

    # Displaying all the fields in admin in different sections.
    readonly_fields = ['joining_date']
    fieldsets = [
        ('User Information', {'fields': ['user', 'name', 'email']}),
        ('Date information', {'fields': ['joining_date'], 'classes': ['collapse']}),
    ]

    list_display = ['user', 'name', 'email', 'joining_date']
    list_filter = ['joining_date']
    search_fields = ['name']

    class Meta:
        """Information of this class."""

        model = UserProfile


class UserProfileInfoAdmin(admin.ModelAdmin):
    """Customising admin view of UserProfileInfo class."""

    '''Displaying all the fields in admin in order.'''
    # fields = ['user', 'gender', 'full_name']

    '''Displaying all the fields in admin in different sections.'''
    # readonly_fields = ['joining_date']
    fieldsets = [
        ('User Information', {'fields': ['full_name', 'gender', 'profile_picture']}),
        # ('Date information', {'fields': ['joining_date'], 'classes': ['collapse']}),
    ]

    list_display = ['full_name', 'gender', 'profile_picture']
    # list_filter = ['user__joining_date']
    search_fields = ['name']

    class Meta:
        """Information of this class."""

        model = UserProfileInfo

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
