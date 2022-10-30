# Generated by Django 4.0.5 on 2022-09-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_firstname_enquiry_fullname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='fullname',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='firstname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='secondname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
