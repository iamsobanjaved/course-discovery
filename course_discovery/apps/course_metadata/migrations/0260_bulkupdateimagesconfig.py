# Generated by Django 2.2.16 on 2020-12-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0259_depr_program_card_image_url_and_add_exec_ed_cert_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkUpdateImagesConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_urls', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]