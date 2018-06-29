from django.db import models

# Create your models here.
class WorldCupTeam(models.Model):
    #队名、小组、每场小组赛的时间和得分以及对手得分、净胜球、积分
    name = models.CharField(max_length = 20)
    group = models.CharField(max_length = 20)
    firsrgame_time = models.DateTimeField()
    firstgame_score = models.IntegerField(default = 0)
    firstgame_competitor = models.IntegerField(default = 0)
    secondgame_time = models.DateTimeField()
    secondgame_score = models.IntegerField(default = 0)
    secondgame_competitor = models.IntegerField(default = 0)
    thirdgame_time = models.DateTimeField()
    thirdgame_score = models.IntegerField(default = 0)
    thirdgame_competitor = models.IntegerField(default = 0)
    GD = models.IntegerField(default = 0)
    integral = models.IntegerField(default = 0)
