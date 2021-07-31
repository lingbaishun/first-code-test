# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:50:26 2018

@author: LBS
"""

from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question']
        }),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        }),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
# Register your models here.
