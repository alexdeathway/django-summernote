# Generated by Django 3.2.23 on 2023-12-04 07:33

import archiver.storage_backend
from django.db import migrations, models
import django_summernote.utils


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0003_alter_attachment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(storage=archiver.storage_backend.MediaStorage(), upload_to=django_summernote.utils.uploaded_filepath),
        ),
    ]