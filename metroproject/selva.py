# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class MetroappAddmoney(models.Model):
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    card_no = models.CharField(max_length=20, blank=True, null=True)
    upi_id = models.CharField(max_length=200, blank=True, null=True)
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    selected_amount = models.CharField(max_length=20, blank=True, null=True)
    host_balance = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metroapp_addmoney'


class MetroappBuyticket(models.Model):
    source = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    fare_amount = models.IntegerField(blank=True, null=True)
    return_type = models.CharField(max_length=10, blank=True, null=True)
    upi_pin = models.CharField(max_length=200, blank=True, null=True)
    order_id = models.CharField(max_length=200, blank=True, null=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    ticket_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metroapp_buyticket'


class MetroappCardcreation(models.Model):
    card_no = models.CharField(max_length=20, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    salutation = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.CharField(max_length=50, blank=True, null=True)
    valid_proof_id = models.CharField(max_length=50, blank=True, null=True)
    valid_proof_no = models.CharField(max_length=100, blank=True, null=True)
    pan_no = models.CharField(max_length=100, blank=True, null=True)
    application_id = models.CharField(max_length=100, blank=True, null=True)
    otp_no = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metroapp_cardcreation'


class MetroappCarddetails(models.Model):
    card_no = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metroapp_carddetails'


class MetroappCitylist(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metroapp_citylist'


class MetroappFareaount(models.Model):
    source = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    fare_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metroapp_fareaount'


class MetroappLogin(models.Model):
    user_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    otp_no = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metroapp_login'


class MetroappRegister(models.Model):
    user_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100, blank=True, null=True)
    communication_address = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile_no = models.CharField(max_length=100, blank=True, null=True)
    permenent_address = models.CharField(max_length=250, blank=True, null=True)
    picture = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'metroapp_register'
