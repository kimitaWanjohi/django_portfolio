# Generated by Django 4.1.2 on 2022-11-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_eductation_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]