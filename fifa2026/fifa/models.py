from django.db import models
from django.utils.html import format_html

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    flag_image = models.ImageField(upload_to='media', null=False, blank=False)
    emblem = models.ImageField(upload_to='media', null=False, blank=False)
    
    def __str__(self):
            return self.team_name
        
    def show_flag_image(self):
        return format_html('<img src="{}" width="100" />', self.flag_image.url)

    def show_emblem(self):
        return format_html('<img src="{}" width="100" />', self.emblem.url)

 
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'Equipos'
        ordering = ['id']

class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Posición'
        verbose_name_plural = 'Posiciones'
        db_table = 'Posicion'
        ordering = ['id']

class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    player_photo = models.ImageField(upload_to='media', null=False, blank=False)
    date_of_birth = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    jersey_number = models.IntegerField()
    is_starter = models.BooleanField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def show_player_photo(self):
        return format_html('<img src="{}" width="100" />', self.player_photo.url)

  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'Jugadores'
        ordering = ['id']

class Coach(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    teams = models.ForeignKey(Team, on_delete=models.CASCADE)

    ROLE_CHOICES = [
        ('Técnico', 'Técnico'),
        ('Asistente', 'Asistente'),
        ('Médico', 'Médico'),
        ('Preparador', 'Preparador'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, help_text='Seleccione el rol')
    NATIONALITY_CHOICES = [
        ('AFG', 'Afghanistan'),
        ('ALB', 'Albania'),
        ('DZA', 'Algeria'),
        ('AND', 'Andorra'),
        ('AGO', 'Angola'),
        ('ARG', 'Argentina'),
        ('ARM', 'Armenia'),
        ('AUS', 'Australia'),
        ('AUT', 'Austria'),
        ('AZE', 'Azerbaijan'),
        ('BHR', 'Bahrain'),
        ('BGD', 'Bangladesh'),
        ('BLR', 'Belarus'),
        ('BEL', 'Belgium'),
        ('BEN', 'Benin'),
        ('BTN', 'Bhutan'),
        ('BOL', 'Bolivia'),
        ('BIH', 'Bosnia and Herzegovina'),
        ('BRA', 'Brazil'),
        ('BRN', 'Brunei'),
        ('BGR', 'Bulgaria'),
        ('BFA', 'Burkina Faso'),
        ('BDI', 'Burundi'),
        ('KHM', 'Cambodia'),
        ('CMR', 'Cameroon'),
        ('CAN', 'Canada'),
        ('CPV', 'Cape Verde'),
        ('CAF', 'Central African Republic'),
        ('TCD', 'Chad'),
        ('CHL', 'Chile'),
        ('CHN', 'China'),
        ('COL', 'Colombia'),
        ('COM', 'Comoros'),
        ('COG', 'Congo'),
        ('CRI', 'Costa Rica'),
        ('HRV', 'Croatia'),
        ('CUB', 'Cuba'),
        ('CYP', 'Cyprus'),
        ('CZE', 'Czech Republic'),
        ('DNK', 'Denmark'),
        ('DJI', 'Djibouti'),
        ('DOM', 'Dominican Republic'),
        ('ECU', 'Ecuador'),
        ('EGY', 'Egypt'),
        ('SLV', 'El Salvador'),
]

    nationality = models.CharField(max_length=255, choices=NATIONALITY_CHOICES, help_text='Seleccione la nacionalidad')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        db_table = 'Tecnico'
        ordering = ['id']
