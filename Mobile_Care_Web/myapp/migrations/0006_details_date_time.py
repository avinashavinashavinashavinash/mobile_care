# Generated by Django 4.2.1 on 2023-11-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_details_complaint_alter_details_customer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='date_time',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]