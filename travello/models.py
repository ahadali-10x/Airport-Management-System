# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Airplane(models.Model):
    registration_num = models.IntegerField(db_column='Registration_num', primary_key=True)  # Field name made lowercase.
    model = models.ForeignKey('PlaneType', models.DO_NOTHING, db_column='Model', blank=True, null=True)  # Field name made lowercase.
    hangar_num = models.ForeignKey('Hangar', models.DO_NOTHING, db_column='Hangar_num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'airplane'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Coorporation(models.Model):
    co_name = models.CharField(db_column='Co_name', primary_key=True, max_length=20)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone_num = models.IntegerField(db_column='Phone_num', blank=True, null=True)  # Field name made lowercase.
    owner = models.ForeignKey('Owner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coorporation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Employee(models.Model):
    essn = models.OneToOneField('Person', models.DO_NOTHING, db_column='ESSN', primary_key=True)  # Field name made lowercase.
    shift_num = models.IntegerField(db_column='Shift_num')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Flies(models.Model):
    pssn = models.OneToOneField('Pilot', models.DO_NOTHING, db_column='PSSN', primary_key=True)  # Field name made lowercase.
    model = models.ForeignKey('PlaneType', models.DO_NOTHING, db_column='Model')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flies'
        unique_together = (('pssn', 'model'),)


class Hangar(models.Model):
    hangar_num = models.IntegerField(db_column='Hangar_num', primary_key=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hangar'


class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    owner_name = models.CharField(db_column='Owner_name', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'owner'


class Owns(models.Model):
    owner = models.OneToOneField(Owner, models.DO_NOTHING, primary_key=True)
    registration_num = models.ForeignKey(Airplane, models.DO_NOTHING, db_column='Registration_num')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'owns'
        unique_together = (('owner', 'registration_num'),)


class Person(models.Model):
    ssn = models.IntegerField(db_column='SSN', primary_key=True)  # Field name made lowercase.
    person_name = models.CharField(db_column='Person_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    owner = models.ForeignKey(Owner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Pilot(models.Model):
    pssn = models.OneToOneField(Person, models.DO_NOTHING, db_column='PSSN', primary_key=True)  # Field name made lowercase.
    lic_num = models.IntegerField(db_column='Lic_num')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pilot'


class PlaneType(models.Model):
    model = models.IntegerField(db_column='Model', primary_key=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plane_type'


class Service(models.Model):
    registration_num = models.OneToOneField(Airplane, models.DO_NOTHING, db_column='Registration_num', primary_key=True)  # Field name made lowercase.
    service_date = models.DateField(db_column='Service_date', blank=True, null=True)  # Field name made lowercase.
    service_time = models.TimeField(db_column='Service_time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'


class WorksOn(models.Model):
    essn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ESSN', primary_key=True)  # Field name made lowercase.
    model = models.ForeignKey(PlaneType, models.DO_NOTHING, db_column='Model')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'works_on'
        unique_together = (('essn', 'model'),)

