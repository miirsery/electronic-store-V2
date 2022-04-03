# Generated by Django 4.0.3 on 2022-04-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.PositiveIntegerField(choices=[(1, '1 - Terribly'), (2, '2 - Bad'), (3, '3 - Normal'), (4, '4 - Okay'), (5, '5 - Amazing')], null=True),
        ),
    ]
