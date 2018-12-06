from django.contrib import admin

from game.models import Crop, CropSpecies, CropSpeciesRewardDetail
from item.models import ItemPrototype


class CropAdmin(admin.ModelAdmin):

    def name(self, instance):
        return instance.crop_species.name
    def cell(self, instance):
        return instance.cell

    model = Crop
    list_display = ['id', 'name', 'cell', 'status', 'created_at']
    ordering = ['created_at', 'id']
    inlines = []


class RewardChoicesInline(admin.TabularInline):
    model = CropSpeciesRewardDetail
    max_num = 0
    extra = 0
    readonly_fields = []
    fields = readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False


class CropSpeciesAdmin(admin.ModelAdmin):

    # def name(self, instance):
    #     return instance.crop_species.name
    # def cell(self, instance):
    #     return instance.cell

    model = Crop
    list_display = ['id', 'name', 'code', 'base_ripening_age', 'base_growing_speed']
    ordering = ['id']
    inlines = [RewardChoicesInline]


admin.site.register(Crop, CropAdmin)
admin.site.register(CropSpecies, CropSpeciesAdmin)
