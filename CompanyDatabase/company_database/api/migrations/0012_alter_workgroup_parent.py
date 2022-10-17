# Generated by Django 4.1.2 on 2022-10-14 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_workgroup_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgroup',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subGroups', to='api.workgroup'),
        ),
    ]
