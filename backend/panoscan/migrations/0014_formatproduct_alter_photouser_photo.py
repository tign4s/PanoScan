# Generated by Django 5.0.6 on 2024-07-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panoscan', '0013_photouser_active_alter_photouser_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_in_mm', models.IntegerField()),
                ('width_in_mm', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='photouser',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]