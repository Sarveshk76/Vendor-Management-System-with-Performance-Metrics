# Generated by Django 4.2.7 on 2023-11-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='average_response_time',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='fulfillment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='quality_rating_avg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(default=0),
        ),
    ]
