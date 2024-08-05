# Generated by Django 5.0.4 on 2024-08-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataticket',
            name='id',
        ),
        migrations.AddField(
            model_name='dataticket',
            name='accept_staff_name',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='dataticket',
            name='date_create_ticket',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='dataticket',
            name='id_ticket',
            field=models.CharField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataticket',
            name='username_create_ticket',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='dataticket',
            name='date_accept_ticket',
            field=models.DateTimeField(null=True),
        ),
    ]