# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fulltext(models.Model):
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')
    fulltext = models.CharField(db_column='fullText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(auto_now_add=True)
    fullrepeat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fulltext'


class Integral(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')
    number = models.IntegerField()
    begintime = models.DateTimeField(auto_now_add=True)
    overtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integral'


class Paragraphtext(models.Model):
    textid = models.ForeignKey(Fulltext, models.DO_NOTHING, db_column='textId')  # Field name made lowercase.
    paragraph = models.CharField(max_length=255, blank=True, null=True)
    repeat = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paragraphtext'


class Topup(models.Model):
    id = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')
    ordernumber = models.IntegerField(blank=True, null=True)
    topuptime = models.DateTimeField(auto_now_add=True)
    many = models.CharField(max_length=255)
    details = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'topup'


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'
