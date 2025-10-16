from django.contrib import admin
from .models import Car
from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter


# Register your models here.

class StateUsedFilter(SimpleListFilter):
    title = 'state'
    parameter_name = 'state'

    def lookups(self, request, model_admin):
        states = model_admin.model.objects.values_list('state', flat=True).distinct()
        state_choices = dict(model_admin.model._meta.get_field('state').choices)
        return [(state, state_choices.get(state, state)) for state in states if state]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(state=self.value())
        return queryset

    

class CarAdmin(admin.ModelAdmin):
   def thumbnail(self,object):
        return format_html('<img src="{}"width="40" style="border-radius:50px">'.format(object.car_photo.url))
  
   list_display=('id','thumbnail','car_title','city','year','color','body_style','fuel_type','price','is_featured',) 
   list_display_links=('id','thumbnail','car_title')
   search_fields=('car_title','id','city','model','body_style','fuel_type')
   list_editable=('is_featured',)
   list_filter=(StateUsedFilter,'city','car_make','car_title','fuel_type')







admin.site.register(Car,CarAdmin)