# Generated by Django 4.1.4 on 2023-01-29 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbcFamilies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('family_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_address', models.CharField(blank=True, max_length=100, null=True)),
                ('google_suggested_address', models.CharField(blank=True, max_length=100, null=True)),
                ('neigborhood', models.CharField(blank=True, db_column='Neigborhood', max_length=100, null=True)),
                ('lga', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('coordinates', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'abc_families',
                'db_table': 'abc_families',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'calendar',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('maiden_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('second_phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_address', models.CharField(blank=True, max_length=100, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=100, null=True)),
                ('lga', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_state', models.CharField(blank=True, max_length=100, null=True)),
                ('lat_lng', models.CharField(blank=True, max_length=100, null=True)),
                ('state_of_origin', models.CharField(blank=True, max_length=100, null=True)),
                ('state_lga', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=100, null=True)),
                ('wedding_date', models.CharField(blank=True, max_length=100, null=True)),
                ('baptism', models.CharField(blank=True, max_length=100, null=True)),
                ('society', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'members',
                'db_table': 'members',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Visitations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('day_visited', models.CharField(blank=True, max_length=100, null=True)),
                ('condition', models.CharField(blank=True, max_length=100, null=True)),
                ('scheduled_visitation', models.DateField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('visitation_status', models.BooleanField(blank=True, null=True)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.abcfamilies')),
            ],
            options={
                'db_table': 'visitations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.CharField(blank=True, max_length=100, null=True)),
                ('end_date', models.CharField(blank=True, max_length=100, null=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.members')),
            ],
            options={
                'verbose_name_plural': 'positions',
                'db_table': 'positions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='JointEvents',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=120, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=500, null=True)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('event_completed', models.DateField(blank=True, null=True)),
                ('calendar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.calendar')),
                ('visitation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.visitations')),
            ],
            options={
                'db_table': 'joint_events',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='abcfamilies',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.members'),
        ),
    ]
