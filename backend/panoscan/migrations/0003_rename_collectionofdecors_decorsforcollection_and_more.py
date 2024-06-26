# Generated by Django 5.0.6 on 2024-06-26 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panoscan', '0002_decor_ncs_equivalent_structure_producer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CollectionOfDecors',
            new_name='DecorsForCollection',
        ),
        migrations.RemoveField(
            model_name='decor',
            name='panel_type',
        ),
        migrations.CreateModel(
            name='PanelTypesForStructureDecorCombination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decor_structure_combination', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='panoscan.structuresfordecor')),
                ('panel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panoscan.paneltype')),
            ],
            options={
                'unique_together': {('decor_structure_combination', 'panel_type')},
            },
        ),
        migrations.AddField(
            model_name='structuresfordecor',
            name='panel_type',
            field=models.ManyToManyField(through='panoscan.PanelTypesForStructureDecorCombination', to='panoscan.paneltype'),
        ),
        migrations.DeleteModel(
            name='PanelTypesForDecor',
        ),
    ]
