# Generated by Django 4.1.7 on 2023-02-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_feature_details_feature_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='details',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]