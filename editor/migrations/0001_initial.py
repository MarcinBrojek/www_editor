# Generated by Django 3.2 on 2021-05-10 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('validity_flag', models.BooleanField()),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateField()),
                ('availability_flag', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('validity_flag', models.BooleanField()),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateField()),
                ('line_number', models.IntegerField(default=0)),
                ('end_line_number', models.IntegerField(default=0)),
                ('availability_flag', models.BooleanField(default=True)),
                ('result', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('validity_flag', models.BooleanField()),
                ('name', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('validity_flag', models.BooleanField()),
                ('data', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='editor.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('validity_flag', models.BooleanField()),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('line_number', models.IntegerField(default=0)),
                ('end_line_number', models.IntegerField(default=0)),
                ('creation_date', models.DateField()),
                ('availability_flag', models.BooleanField(default=True)),
                ('category', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('parent_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='editor.file')),
                ('parent_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='editor.filesection')),
                ('status_data', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='editor.statusdata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='editor.user'),
        ),
        migrations.AddField(
            model_name='file',
            name='parent_directory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='editor.directory'),
        ),
        migrations.AddField(
            model_name='directory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='editor.user'),
        ),
        migrations.AddField(
            model_name='directory',
            name='parent_directory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='editor.directory'),
        ),
    ]