# Generated by Django 4.1.2 on 2022-10-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_workgroup_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='jobs',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='workGroups',
        ),
        migrations.RemoveField(
            model_name='workgroup',
            name='parent',
        ),
        migrations.AddField(
            model_name='workgroup',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='workGroups', to='api.worker'),
        ),
        migrations.AlterField(
            model_name='job',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='jobs', to='api.worker'),
        ),
    ]
