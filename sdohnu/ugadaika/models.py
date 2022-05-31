from django.db import models

# Create your models here.

class Styles(models.Model):
    id_style = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_start = models.IntegerField()
    date_finish = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'styles'

    def __str__(self):
        return self.name

class Artists(models.Model):
    id_artist = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    biography = models.TextField()
    date_birth = models.IntegerField()
    date_death = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'artists'

    def __str__(self):
        return self.name

class Techniques(models.Model):
    id_technique = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'techniques'

class Genres(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'genres'

class Paintings(models.Model):
    id_painting = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artists, models.DO_NOTHING, db_column='artist')
    genre = models.ForeignKey(Genres, models.DO_NOTHING, db_column='genre')
    style = models.ForeignKey('Styles', models.DO_NOTHING, db_column='style')
    technique = models.ForeignKey('Techniques', models.DO_NOTHING, db_column='technique')
    date = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'paintings'

    def __str__(self):
        return self.name

