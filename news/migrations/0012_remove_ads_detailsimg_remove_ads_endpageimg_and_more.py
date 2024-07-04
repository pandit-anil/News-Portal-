# Generated by Django 5.0.6 on 2024-07-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='detailsimg',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='endpageimg',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='footerimg',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='headerimg',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='mostpopularimg',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='whatsnewimg',
        ),
        migrations.AddField(
            model_name='ads',
            name='image',
            field=models.ImageField(height_field='image_height', null=True, upload_to='ads/', width_field='image_width'),
        ),
        migrations.AddField(
            model_name='ads',
            name='image_height',
            field=models.PositiveIntegerField(default=500),
        ),
        migrations.AddField(
            model_name='ads',
            name='image_type',
            field=models.CharField(choices=[('whatnewimage', 'WhatsNewImage'), ('mostpopularimg', 'MostPopularImg'), ('endpageimg', 'endpageimg')], default='whatnewimage', max_length=200),
        ),
        migrations.AddField(
            model_name='ads',
            name='image_width',
            field=models.PositiveIntegerField(default=500),
        ),
    ]