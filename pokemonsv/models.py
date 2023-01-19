from django.db import models

class Pokemons(models.Model):
    
    dex_no = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10)
    form = models.CharField(max_length=20, blank=True, null=True)
    type1 = models.CharField(max_length=10, blank=True, null=True)
    type2 = models.CharField(max_length=10, blank=True, null=True)
    ability1 = models.CharField(max_length=20, blank=True, null=True)
    ability2 = models.CharField(max_length=20, blank=True, null=True)
    ability_d = models.CharField(max_length=20, blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    sp_attack = models.IntegerField(blank=True, null=True)
    sp_defence = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemons'
    
    def __str__(self):
        return self.name


class Moves(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=20, blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    accury = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    direct = models.IntegerField(blank=True, null=True)
    number_times_max = models.IntegerField(blank=True, null=True)
    number_times_min = models.IntegerField(blank=True, null=True)
    on_hit = models.IntegerField(blank=True, null=True)
    machine_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves'
    
    def __str__(self):
        return self.name


