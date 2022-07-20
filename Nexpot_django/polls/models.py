from pickle import TRUE
from django.db import models


class Comments(models.Model):
    commid = models.CharField(db_column='commID', primary_key=True, max_length=20)  # Field name made lowercase.
    videoid = models.ForeignKey('Youtube', models.DO_NOTHING, db_column='videoID')  # Field name made lowercase.
    reply = models.TextField(blank=True, null=True)
    replylikes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Places(models.Model):
    idx = models.IntegerField()
    videoid = models.ForeignKey('Youtube', models.DO_NOTHING, db_column='videoID')  # Field name made lowercase.
    placeid = models.CharField(db_column='placeID', primary_key=True, max_length=12)  # Field name made lowercase.
    pname = models.CharField(max_length=20)
    paddress = models.CharField(max_length=50)
    pdo = models.CharField(max_length=10, blank=True, null=True)
    psi = models.CharField(max_length=15, blank=True, null=True)
    pphone = models.CharField(max_length=13, blank=True, null=True)
    pdaumurl = models.CharField(db_column='pdaumURL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    px = models.FloatField(db_column='pX')  # Field name made lowercase.
    py = models.FloatField(db_column='pY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'places'

    def __str__(self):
        return self.pname


class Youtube(models.Model):
    videoid = models.CharField(db_column='videoID', primary_key=True, max_length=11, unique=TRUE)  # Field name made lowercase.
    channelname = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=48, blank=True, null=True)
    youtime = models.DateField()
    views = models.IntegerField(blank=True, null=True)
    youtlikes = models.IntegerField(blank=True, null=True)
    lencomments = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'youtube'

    def __str__(self):
        return self.videoid

class YoutubeVO(models.Model):
    Youtube,
    pname = models.CharField(max_length=20)

    
    class Meta:
        managed = False
        db_table = 'youtube'

    def __str__(self):
        return self.title
