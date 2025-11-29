from django.contrib import admin
from .models import *
# Register your models here.


# we can also customize the admin panel for our models by creating admin classes
class ChaiReviewInline(admin.TabularInline): # to show reviews inline in chai varity admin page not show in separate page
    model = ChaiReview
    extra = 1  # number of extra forms to display
    
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'price', 'created_at', )
    search_fields = ('name', 'chai_type')
    list_filter = ('chai_type', 'created_at')
    inlines = [ChaiReviewInline]  # to show reviews inline in chai varity admin page
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)  # to show many to many field with horizontal filter widget

    
class ChaiCertificationAdmin(admin.ModelAdmin):
    list_display = ('certification_name', 'chai', 'issue_date', 'expiry_date',)

    
    
    
    
# for see our model in admin panel we need to register it here
admin.site.register(ChaiVarity, ChaiVarityAdmin)
# admin.site.register(ChaiReview,ChaiReviewInline)
admin.site.register(Store, StoreAdmin) 
admin.site.register(ChaiCertification, ChaiCertificationAdmin)