from django.db import models

__all__ = ('Page', 'API',)


class Page(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'app_pages'


class API(models.Model):
    path = models.CharField(max_length=200, null=False, blank=False)
    page = models.ForeignKey(Page, on_delete=models.DO_NOTHING, related_name='pages')
    created_at = models.DateTimeField(auto_now_add=True)

    version = models.IntegerField(default=1)

    class Meta:
        db_table = 'app_apis'
