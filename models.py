# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agency(models.Model):
    agency_id = models.TextField(blank=True, null=True)
    agency_name = models.TextField(blank=True, null=True)
    agency_url = models.TextField(blank=True, null=True)
    agency_timezone = models.TextField(blank=True, null=True)
    agency_lang = models.TextField(blank=True, null=True)
    agency_phone = models.TextField(blank=True, null=True)
    agency_fare_url = models.TextField(blank=True, null=True)
    agency_email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agency'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calendar(models.Model):
    service_id = models.BigIntegerField(blank=True, null=True)
    monday = models.BigIntegerField(blank=True, null=True)
    tuesday = models.BigIntegerField(blank=True, null=True)
    wednesday = models.BigIntegerField(blank=True, null=True)
    thursday = models.BigIntegerField(blank=True, null=True)
    friday = models.BigIntegerField(blank=True, null=True)
    saturday = models.BigIntegerField(blank=True, null=True)
    sunday = models.BigIntegerField(blank=True, null=True)
    start_date = models.BigIntegerField(blank=True, null=True)
    end_date = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'


class CalendarDates(models.Model):
    service_id = models.BigIntegerField(blank=True, null=True)
    date = models.BigIntegerField(blank=True, null=True)
    exception_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_dates'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FeedInfo(models.Model):
    feed_publisher_name = models.TextField(blank=True, null=True)
    feed_publisher_url = models.TextField(blank=True, null=True)
    feed_lang = models.TextField(blank=True, null=True)
    feed_start_date = models.BigIntegerField(blank=True, null=True)
    feed_end_date = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feed_info'


class HomePost(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    title = models.CharField(max_length=50)
    second_title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'home_post'


class Routes(models.Model):
    route_id = models.BigIntegerField(blank=True, null=True)
    agency_id = models.FloatField(blank=True, null=True)
    route_short_name = models.TextField(blank=True, null=True)
    route_long_name = models.TextField(blank=True, null=True)
    route_desc = models.FloatField(blank=True, null=True)
    route_type = models.BigIntegerField(blank=True, null=True)
    route_url = models.FloatField(blank=True, null=True)
    route_color = models.TextField(blank=True, null=True)
    route_text_color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'


class Shapes(models.Model):
    shape_id = models.BigIntegerField(blank=True, null=True)
    shape_pt_lat = models.FloatField(blank=True, null=True)
    shape_pt_lon = models.FloatField(blank=True, null=True)
    shape_pt_sequence = models.BigIntegerField(blank=True, null=True)
    shape_dist_traveled = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shapes'


class StopTimes(models.Model):
    trip_id = models.BigIntegerField(blank=True, null=True)
    arrival_time = models.TextField(blank=True, null=True)
    departure_time = models.TextField(blank=True, null=True)
    stop_id = models.BigIntegerField(blank=True, null=True)
    stop_sequence = models.BigIntegerField(blank=True, null=True)
    stop_headsign = models.FloatField(blank=True, null=True)
    pickup_type = models.FloatField(blank=True, null=True)
    drop_off_type = models.FloatField(blank=True, null=True)
    shape_dist_traveled = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stop_times'


class Stops(models.Model):
    stop_id = models.BigIntegerField(blank=True, null=True)
    stop_code = models.FloatField(blank=True, null=True)
    stop_name = models.TextField(blank=True, null=True)
    stop_desc = models.FloatField(blank=True, null=True)
    stop_lat = models.FloatField(blank=True, null=True)
    stop_lon = models.FloatField(blank=True, null=True)
    stop_url = models.FloatField(blank=True, null=True)
    location_type = models.FloatField(blank=True, null=True)
    parent_station = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stops'


class Transfers(models.Model):
    from_stop_id = models.BigIntegerField(blank=True, null=True)
    to_stop_id = models.BigIntegerField(blank=True, null=True)
    transfer_type = models.BigIntegerField(blank=True, null=True)
    min_transfer_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfers'


class Trips(models.Model):
    route_id = models.BigIntegerField(blank=True, null=True)
    service_id = models.BigIntegerField(blank=True, null=True)
    trip_id = models.BigIntegerField(blank=True, null=True)
    trip_headsign = models.FloatField(blank=True, null=True)
    trip_short_name = models.FloatField(blank=True, null=True)
    direction_id = models.BigIntegerField(blank=True, null=True)
    block_id = models.BigIntegerField(blank=True, null=True)
    shape_id = models.BigIntegerField(blank=True, null=True)
    wheelchair_accessible = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'
