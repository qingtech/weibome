# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class WbGeo(models.Model):
    id = models.IntegerField(primary_key=True)
    longitude = models.CharField(max_length=45, blank=True)
    latitude = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=45, blank=True)
    province = models.CharField(max_length=45, blank=True)
    city_name = models.CharField(max_length=45, blank=True)
    province_name = models.CharField(max_length=45, blank=True)
    address = models.CharField(max_length=45, blank=True)
    pinyin = models.CharField(max_length=45, blank=True)
    more = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'wb_geo'

class WbUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idstr = models.CharField(max_length=45, blank=True)
    screen_name = models.CharField(max_length=45, blank=True)
    name = models.CharField(max_length=45, blank=True)
    province = models.IntegerField(null=True, blank=True)
    city = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=400, blank=True)
    url = models.CharField(max_length=45, blank=True)
    profile_image_url = models.CharField(max_length=45, blank=True)
    profile_url = models.CharField(max_length=45, blank=True)
    domain = models.CharField(max_length=45, blank=True)
    weihao = models.CharField(max_length=45, blank=True)
    gender = models.CharField(max_length=12, blank=True)
    followers_count = models.IntegerField(null=True, blank=True)
    friends_count = models.IntegerField(null=True, blank=True)
    statuses_count = models.IntegerField(null=True, blank=True)
    favourites_count = models.IntegerField(null=True, blank=True)
    created_at = models.CharField(max_length=75, blank=True)
    following = models.BooleanField()
    allow_all_act_msg = models.BooleanField()
    geo_enabled = models.BooleanField()
    verified = models.BooleanField()
    verified_type = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=100, blank=True)
    status = models.BigIntegerField()
    allow_all_comment = models.BooleanField()
    avatar_large = models.CharField(max_length=45, blank=True)
    avatar_hd = models.CharField(max_length=45, blank=True)
    verified_reason = models.CharField(max_length=400, blank=True)
    follow_me = models.CharField(max_length=45, blank=True)
    online_status = models.IntegerField(null=True, blank=True)
    bi_followers_count = models.IntegerField(null=True, blank=True)
    lang = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'wb_user'

class WbStatus(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    id = models.BigIntegerField(primary_key=True)
    mid = models.BigIntegerField()
    idstr = models.CharField(max_length=20, blank=True)
    text = models.CharField(max_length=400, blank=True)
    source = models.CharField(max_length=100, blank=True)
    favorited = models.BooleanField()
    truncated = models.BooleanField()
    in_reply_to_status_id = models.CharField(max_length=20, blank=True)
    in_reply_to_user_id = models.CharField(max_length=20, blank=True)
    in_reply_to_screen_name = models.CharField(max_length=70, blank=True)
    thumbnail_pic = models.CharField(max_length=100, blank=True)
    bmiddle_pic = models.CharField(max_length=100, blank=True)
    original_pic = models.CharField(max_length=100, blank=True)
    geo = models.ForeignKey(WbGeo, related_name='status_geo')
    user = models.ForeignKey(WbUser, related_name='status_owner')
    retweeted_status = models.ForeignKey('self', null=True, blank=True, default=None, related_name='status_retweeted')
    reposts_count = models.IntegerField(null=True, blank=True)
    comments_count = models.IntegerField(null=True, blank=True)
    attitudes_count = models.IntegerField(null=True, blank=True)
    mlevel = models.IntegerField(null=True, blank=True)
    visible = models.CharField(max_length=400, blank=True)
    pic_ids = models.CharField(max_length=400, blank=True)
    ad = models.CharField(max_length=400, blank=True)
    class Meta:
        db_table = u'wb_status'


# Create your models here.
class WeiboApp(models.Model):
	app_name = models.CharField(max_length = 25)
	app_key = models.CharField(max_length = 25)
	app_secret = models.CharField(max_length = 50)
	callback_url = models.CharField(max_length = 50)

	def __str__(self):
		if self.app_name:
			return self.app_name
		else:
			return 'unknown'
