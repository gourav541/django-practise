# Generated by Django 4.1.7 on 2023-02-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_feature_details_alter_feature_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='details',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
