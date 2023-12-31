# Generated by Django 4.2.1 on 2023-11-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_details_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='complaint',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='customer_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='mobile_model',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='mobile_number',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='remark_status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='roll_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='details',
            name='technition',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
