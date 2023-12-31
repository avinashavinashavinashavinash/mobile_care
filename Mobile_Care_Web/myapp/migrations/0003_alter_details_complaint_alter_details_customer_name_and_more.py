# Generated by Django 4.2.1 on 2023-11-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_staff_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='complaint',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='customer_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='mobile_model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='remark_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='roll_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='technition',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
