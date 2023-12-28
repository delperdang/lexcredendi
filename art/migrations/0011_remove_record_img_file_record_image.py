# Generated by Django 5.0 on 2023-12-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0010_alter_record_img_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='img_file',
        ),
        migrations.AddField(
            model_name='record',
            name='image',
            field=models.ImageField(default=None, upload_to='art/img', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
