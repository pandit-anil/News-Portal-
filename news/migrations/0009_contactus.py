# Generated by Django 5.0.6 on 2024-06-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_systemsetting_facebooklink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mess', models.TextField()),
                ('subject', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]