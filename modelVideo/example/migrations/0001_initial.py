# Generated by Django 2.2.7 on 2019-11-28 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('creator', models.CharField(max_length=20)),
                ('paradigm', models.CharField(max_length=20)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.Company')),
                ('languages', models.ManyToManyField(to='example.Languages')),
            ],
        ),
    ]
