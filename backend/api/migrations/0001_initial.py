# Generated by Django 2.2.7 on 2019-12-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remuneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edinet_code', models.CharField(max_length=6)),
                ('sec_code', models.CharField(max_length=5)),
                ('filer_name', models.TextField()),
                ('doc_description', models.TextField()),
                ('doc_id', models.CharField(max_length=8)),
                ('period_start', models.CharField(max_length=10)),
                ('period_end', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
    ]
