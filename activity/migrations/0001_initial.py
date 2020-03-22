# Generated by Django 2.2.5 on 2020-01-03 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('ShowUnit', models.CharField(max_length=30)),
                ('discontinfo', models.CharField(max_length=30)),
                ('descriptionFilterHtml', models.CharField(max_length=30)),
                ('imageUrl', models.CharField(max_length=30)),
                ('masterUnit', models.CharField(max_length=30)),
                ('webSales', models.CharField(max_length=30)),
                ('sourceWebPromote', models.CharField(max_length=30)),
                ('time', models.DateField(max_length=30)),
                ('endtime', models.DateField(max_length=30)),
                ('onSales', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('comment', models.CharField(default='', max_length=30)),
                ('editModifyDate', models.CharField(default='', max_length=30)),
                ('period', models.CharField(default='', max_length=30)),
                ('locationName', models.CharField(default='', max_length=30)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.Venue')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
