from django.contrib import admin
from myworldcup.models import WorldCupTeam

# Register your models here.
class WorldCupTeamAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'group',
        'firsrgame_time',
        'firstgame_score',
        'firstgame_competitor',
        'secondgame_time',
        'secondgame_score',
        'secondgame_competitor',
        'thirdgame_time',
        'thirdgame_score',
        'thirdgame_competitor',
        'GD',
        'integral',
    ]

admin.site.register(WorldCupTeam, WorldCupTeamAdmin)