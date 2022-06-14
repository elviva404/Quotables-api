# Generated by Django 4.0.5 on 2022-06-14 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotables', '0003_auto_20210105_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='quotables.category'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='profile_image_url',
            field=models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='quotes',
            field=models.ManyToManyField(related_name='+', to='quotables.quote'),
        ),
        migrations.AlterField(
            model_name='category',
            name='quotes',
            field=models.ManyToManyField(related_name='+', to='quotables.quote'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='quotes',
            field=models.ManyToManyField(blank=True, related_name='+', to='quotables.quote'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='apple_music_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='spotify_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='quotes',
            field=models.ManyToManyField(blank=True, related_name='+', to='quotables.quote'),
        ),
    ]
