from django.contrib import admin
from .models import RentalApplication, Promoter
from django.urls import reverse
from django.utils.html import format_html

admin.site.site_header = "Rent A House Admin"
admin.site.site_title = "Rent A House Dashboard"
admin.site.index_title = "Welcome to Rent A House Management"

@admin.register(Promoter)
class PromoterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'tracking_code', 'get_tracking_link')
    search_fields = ('name', 'email', 'tracking_code')

    def get_tracking_link(self, obj):
        url = reverse('apply') + f"?ref={obj.tracking_code}"
        return format_html('<a href="{}" target="_blank">Referral Link</a>', url)
    get_tracking_link.short_description = "Referral Link"

@admin.register(RentalApplication)
class RentalApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'applying_as', 
        'move_in_date', 'submitted_at', 'promoter'
    )
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('applying_as', 'move_in_date', 'submitted_at')
    readonly_fields = ('submitted_at',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'phone_number', 'email')
        }),
        ('Current Address', {
            'fields': ('current_address', 'city', 'state_province', 'zip_postal_code', 'country')
        }),
        ('Employment Details', {
            'fields': ('employer_name', 'job_title', 'monthly_income', 'social_security_number'),
        }),
        ('Identification', {
            'fields': ('id_proof_front', 'id_proof_back', 'photo_selfie')
        }),
        ('Application Details', {
            'fields': ('applying_as', 'move_in_date', 'references', 'additional_comments', 'promoter')
        }),
        ('System Fields', {
            'fields': ('submitted_at',),
        }),
    )

    def has_add_permission(self, request):
        return False

    def delete_queryset(self, request, queryset):
        # Handle bulk deletion
        for obj in queryset:
            obj.delete()
        super().delete_queryset(request, queryset)