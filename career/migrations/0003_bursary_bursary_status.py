# Generated by Django 4.0.3 on 2022-07-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_bursary_faculty_image_institution_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bursary',
            name='bursary_status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=100),
        ),
    ]
