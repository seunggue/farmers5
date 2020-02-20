# Generated by Django 2.2.10 on 2020-02-20 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('help_select', models.CharField(max_length=50)),
                ('people', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('location1', models.CharField(max_length=50)),
                ('location2', models.CharField(max_length=50)),
                ('help_date', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
