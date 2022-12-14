# Generated by Django 4.1.2 on 2022-11-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blogs_project_live_link_project_source_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='eductation',
            name='school',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eductation',
            name='start_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.TextField(),
        ),
    ]
