# Generated by Django 5.1.1 on 2024-10-31 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corduroyserver', '0008_alter_reports_trailname_alter_trails_trailname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='trailName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trails',
            name='trailName',
            field=models.CharField(max_length=100),
        ),
    ]
