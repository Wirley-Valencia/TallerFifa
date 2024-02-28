from django.contrib import admin
from .models import Team, Position, Player, Coach
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'team_name', 'show_flag_image', 'show_emblem',)
    
    class TeamResource(resources.ModelResource):
        class Meta:
            model = Team
            fields = ('id', 'team_name', 'show_flag_image', 'show_emblem',)
            

@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'description',)
    
    class PositionResource(resources.ModelResource):
        class Meta:
            model = Position
            fields = ('id', 'name', 'description',)


@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'show_player_photo', 'date_of_birth', 'position', 'jersey_number', 'is_starter', 'team',)
    
    class PlayerResource(resources.ModelResource):
        class Meta:
            model = Player
            fields =  ('id', 'first_name', 'last_name', 'show_player_photo', 'date_of_birth', 'position', 'jersey_number', 'is_starter', 'team',)

@admin.register(Coach)
class CoachAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'teams', 'role', 'nationality',)
    
    class CoachResource(resources.ModelResource):
        class Meta:
            model = Coach
            fields =  ('id', 'first_name', 'last_name', 'date_of_birth', 'teams', 'role', 'nationality',)




