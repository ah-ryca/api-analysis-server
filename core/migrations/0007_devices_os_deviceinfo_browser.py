# Generated by Django 4.1.2 on 2022-10-14 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_apiresult_alter_api_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=50, null=True)),
                ('version', models.CharField(max_length=50, null=True)),
                ('version_string', models.CharField(max_length=50, null=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='os', to='core.requestinfo')),
            ],
            options={
                'db_table': 'device_os',
            },
        ),
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('family', models.CharField(max_length=50, null=True)),
                ('model', models.CharField(max_length=50, null=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='device_info', to='core.requestinfo')),
            ],
            options={
                'db_table': 'device_info',
            },
        ),
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=50, null=True)),
                ('version', models.CharField(max_length=50, null=True)),
                ('version_string', models.CharField(max_length=50, null=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='browser', to='core.requestinfo')),
            ],
            options={
                'db_table': 'device_browser',
            },
        ),
    ]