# Generated by Django 2.2.5 on 2019-11-05 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import homepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_account', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('school', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cuisine', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('borough', models.CharField(blank=True, max_length=100, null=True)),
                ('building', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Days_left',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('days', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserRequestMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_time', models.DateTimeField(default=homepage.models.in_one_day)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequestmatch_user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequestmatch_user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('service_type', models.CharField(max_length=100)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('school', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('service_status', models.BooleanField(default=True)),
                ('match_status', models.BooleanField(default=False)),
                ('cuisines', models.ManyToManyField(blank=True, to='homepage.Cuisine')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
