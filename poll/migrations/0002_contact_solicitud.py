# Generated by Django 5.1.1 on 2024-10-04 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='solicitud',
            field=models.TextField(default='nnose'),
            preserve_default=False,
        ),
    ]
