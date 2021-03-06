# Generated by Django 4.0.4 on 2022-05-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckStudent',
            fields=[
                ('count', models.AutoField(primary_key=True, serialize=False)),
                ('check_id', models.CharField(max_length=1123)),
                ('check_name', models.CharField(max_length=1123)),
                ('check_major', models.CharField(max_length=1123)),
                ('check_lecture', models.CharField(max_length=1123)),
                ('check_image', models.CharField(max_length=1123)),
                ('check_in_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'check_student',
                'managed': False,
            },
        ),
    ]
