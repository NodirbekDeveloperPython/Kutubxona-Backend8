from django.contrib import admin
from django.contrib.admin import ModelAdmin
from asosiy .models import *

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ('ism', 'id')
    list_display = ('id','ism', 'kitob_soni', 'jins')
    list_display_links = ('ism', 'jins')
    list_editable = ('kitob_soni',)
    list_filter = ('jins', 'kitob_soni')
    list_per_page = 7
    list_max_show_all = 3

@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ('student__ism', 'kitob__nom')
    list_filter = ('qaytardi',)


@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ('nom', 'muallif__ism', 'janr')
    list_filter = ('janr',)

# Register your models here.
admin.site.register(Muallif)
# admin.site.register(Student)
# admin.site.register(Kitob)
# admin.site.register(Record)