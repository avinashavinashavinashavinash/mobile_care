# Generated by Django 4.2.1 on 2023-11-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_details_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='condition',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
