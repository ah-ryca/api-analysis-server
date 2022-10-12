from django.db import models

class RequestInfo(models.Model):
    remote_addr = models.CharField(max_length=20, null=True)
    remote_user = models.CharField(max_length=50, null=True)
    time_local = models.DateTimeField(null=True)
    request = models.CharField(max_length=50, null=True)
    status = models.IntegerField( null=True)
    body_bytes_sent = models.IntegerField(null=True)
    http_referer = models.CharField(max_length=100, null=True)
    http_user_agent = models.CharField(max_length=400, null=True)
    status_type = models.CharField(max_length=50, null=True)
    bytes_sent = models.IntegerField(null=True)
    request_time =  models.DateTimeField(null=True)
    request_path = models.CharField(max_length=100, null=True)
    
    class Meta:
        db_table = 'request_info'
 
