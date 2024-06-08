# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .base_model import BaseModel

class Agency(models.Model):
    agency_id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    agency_name = models.TextField(blank=True, null=True)
    agency_url = models.TextField(blank=True, null=True)
    agency_timezone = models.TextField(blank=True, null=True)
    agency_lang = models.TextField(blank=True, null=True)
    agency_phone = models.TextField(blank=True, null=True)
    agency_fare_url = models.TextField(blank=True, null=True)
    agency_email = models.TextField(blank=True, null=True)


class Calendar(models.Model):
    service_id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    monday = models.BigIntegerField(blank=True, null=True)
    tuesday = models.BigIntegerField(blank=True, null=True)
    wednesday = models.BigIntegerField(blank=True, null=True)
    thursday = models.BigIntegerField(blank=True, null=True)
    friday = models.BigIntegerField(blank=True, null=True)
    saturday = models.BigIntegerField(blank=True, null=True)
    sunday = models.BigIntegerField(blank=True, null=True)
    start_date = models.BigIntegerField(blank=True, null=True)
    end_date = models.BigIntegerField(blank=True, null=True)


class CalendarDates(models.Model):
    service_id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    date = models.BigIntegerField(blank=True, null=True)
    exception_type = models.BigIntegerField(blank=True, null=True)


class FeedInfo(models.Model):
    feed_publisher_name = models.TextField(blank=True, null=True)
    feed_publisher_url = models.TextField(blank=True, null=True)
    feed_lang = models.TextField(blank=True, null=True)
    feed_start_date = models.BigIntegerField(blank=True, null=True)
    feed_end_date = models.BigIntegerField(blank=True, null=True)


class Routes(models.Model):
    route_id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    agency_id = models.ForeignKey(Agency, models.DO_NOTHING, db_column='agency_id', blank=True, null=True)
    route_short_name = models.TextField(blank=True, null=True)
    route_long_name = models.TextField(blank=True, null=True)
    route_desc = models.FloatField(blank=True, null=True)
    route_type = models.BigIntegerField(blank=True, null=True)
    route_url = models.FloatField(blank=True, null=True)
    route_color = models.TextField(blank=True, null=True)
    route_text_color = models.TextField(blank=True, null=True)


class Shapes(models.Model):
    shape_id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    shape_pt_lat = models.FloatField(blank=True, null=True)
    shape_pt_lon = models.FloatField(blank=True, null=True)
    shape_pt_sequence = models.BigIntegerField(blank=True, null=True)
    shape_dist_traveled = models.FloatField(blank=True, null=True)


class StopTimes(models.Model):
    trip_id = models.ForeignKey('Trips', models.DO_NOTHING, db_column='trip_id', blank=True, null=True)
    arrival_time = models.TextField(blank=True, null=True)
    departure_time = models.TextField(blank=True, null=True)
    stop_id = models.ForeignKey('Stops', models.DO_NOTHING, db_column='stop_id', blank=True, null=True)
    stop_sequence = models.BigIntegerField(blank=True, null=True)
    stop_headsign = models.FloatField(blank=True, null=True)
    pickup_type = models.FloatField(blank=True, null=True)
    drop_off_type = models.FloatField(blank=True, null=True)
    shape_dist_traveled = models.FloatField(blank=True, null=True)


class Stops(models.Model):
    stop_id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    stop_code = models.FloatField(blank=True, null=True)
    stop_name = models.TextField(blank=True, null=True)
    stop_desc = models.FloatField(blank=True, null=True)
    stop_lat = models.FloatField(blank=True, null=True)
    stop_lon = models.FloatField(blank=True, null=True)
    stop_url = models.FloatField(blank=True, null=True)
    location_type = models.FloatField(blank=True, null=True)
    parent_station = models.FloatField(blank=True, null=True)


class Transfers(models.Model):
    from_stop_id = models.ForeignKey(Stops, models.DO_NOTHING, db_column='stop_id', blank=True, null=True)
    to_stop_id = models.ForeignKey(Stops, models.DO_NOTHING, db_column='stop_id', blank=True, null=True)
    transfer_type = models.BigIntegerField(blank=True, null=True)
    min_transfer_time = models.BigIntegerField(blank=True, null=True)


class Trips(models.Model):
    route_id = models.ForeignKey(Routes, models.DO_NOTHING, db_column='route_id', blank=True, null=True)
    service_id = models.BigIntegerField(blank=True, null=True)
    trip_id = models.BigIntegerField(blank=True, null=True)
    trip_headsign = models.FloatField(blank=True, null=True)
    trip_short_name = models.FloatField(blank=True, null=True)
    direction_id = models.BigIntegerField(blank=True, null=True)
    block_id = models.BigIntegerField(blank=True, null=True)
    shape_id = models.ForeignKey(Shapes, models.DO_NOTHING, db_column='shape_id', blank=True, null=True)
    wheelchair_accessible = models.FloatField(blank=True, null=True)
