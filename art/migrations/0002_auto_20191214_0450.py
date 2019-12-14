# Generated by Django 3.0 on 2019-12-14 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='code',
        ),
        migrations.RemoveField(
            model_name='record',
            name='work',
        ),
        migrations.AddField(
            model_name='record',
            name='filename',
            field=models.CharField(default='test.jpg', max_length=255, primary_key=True, serialize=False, verbose_name='Filename'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='album',
            field=models.CharField(max_length=255, verbose_name='Album'),
        ),
        migrations.AlterField(
            model_name='record',
            name='rough_date',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Rough Date'),
        ),
    ]
