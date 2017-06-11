from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *



class RSVPAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'guests', 'phone', 'timestamp' )
    fields = ( 'name', 'phone', 'guests', 'note', 'timestamp' )
    readonly_fields = ( 'name', 'phone', 'guests', 'note', 'timestamp' )

admin.site.register(RSVP, RSVPAdmin)


class GiftAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'amount', 'timestamp' )
    fields = ( 'name', 'email', 'note', 'amount', 'raw', 'timestamp' )
    readonly_fields = ( 'name', 'email', 'note', 'amount', 'raw', 'timestamp' )

admin.site.register(Gift, GiftAdmin)


admin.site.unregister(Group)

admin.site.unregister(User)

