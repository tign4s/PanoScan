# Generated by Django 5.0.6 on 2024-06-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panoscan', '0003_rename_collectionofdecors_decorsforcollection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decor',
            name='ncs_equivalent',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
