# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('passenger_type', models.CharField(blank=True, max_length=10)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('traveler_of', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('pnr', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('airline', models.CharField(max_length=50, null=True)),
                ('origin', models.CharField(max_length=100, null=True)),
                ('destination', models.CharField(max_length=100, null=True)),
                ('itinerary', models.CharField(max_length=100, null=True)),
                ('departure_date', models.DateTimeField(null=True)),
                ('return_date', models.DateTimeField(null=True)),
                ('interface_id', models.CharField(max_length=30)),
                ('payement_card', models.CharField(max_length=50, null=True)),
                ('ticketing_pcc', models.CharField(max_length=50, null=True)),
                ('ticketing_agent', models.CharField(max_length=50, null=True)),
                ('ticket_issu_date', models.DateTimeField(blank=True, null=True)),
                ('carriers', models.CharField(max_length=100, null=True)),
                ('validating_carrier', models.CharField(max_length=100, null=True)),
                ('class_of_service', models.CharField(max_length=50, null=True)),
                ('frequent_flyer', models.CharField(blank=True, max_length=50, null=True)),
                ('booking_pcc', models.CharField(blank=True, max_length=50, null=True)),
                ('booking_agent', models.CharField(blank=True, max_length=50, null=True)),
                ('is_ticketed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SchedChange',
            fields=[
                ('pnr', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dk', models.CharField(max_length=30)),
                ('cc_agent', models.CharField(max_length=30)),
                ('t_pcc', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('pax_names', models.CharField(blank=True, default='ANY', max_length=500)),
                ('is_ticket', models.BooleanField(default=False)),
                ('booking_pcc', models.CharField(blank=True, max_length=50, null=True)),
                ('booking_agent', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SegmentSched',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('airline', models.CharField(blank=True, max_length=50, null=True)),
                ('fligthno', models.CharField(blank=True, max_length=50, null=True)),
                ('origin', models.CharField(blank=True, max_length=50, null=True)),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('departure_date', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('arrival_date', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('pnr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gds.SchedChange')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tkt_number', models.CharField(blank=True, max_length=50, null=True)),
                ('ticketing_issu_date', models.CharField(max_length=50, null=True)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gds.Passenger')),
                ('pnr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gds.Reservation')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='passengers',
            field=models.ManyToManyField(related_name='passengers', through='gds.Travel', to='gds.Passenger'),
        ),
        migrations.AlterUniqueTogether(
            name='passenger',
            unique_together=set([('firstname', 'lastname', 'birthdate')]),
        ),
        migrations.AlterUniqueTogether(
            name='travel',
            unique_together=set([('pnr', 'passenger')]),
        ),
    ]
