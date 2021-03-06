# Generated by Django 4.0.5 on 2022-06-14 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotables', '0007_alter_artist_profile_image_url_alter_category_quotes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='profile_image_url',
            field=models.FileField(blank=True, null=True, upload_to='media/artist/'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='image_url',
            field=models.FileField(null=True, upload_to='media/mood/'),
        ),
        migrations.RemoveField(
            model_name='quote',
            name='mood',
        ),
        migrations.AddField(
            model_name='quote',
            name='mood',
            field=models.ManyToManyField(related_name='+', to='quotables.mood'),
        ),
    ]
