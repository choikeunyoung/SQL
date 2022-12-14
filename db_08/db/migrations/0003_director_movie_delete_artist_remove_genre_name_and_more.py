# Generated by Django 4.0.6 on 2022-08-25 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('debut', models.DateTimeField()),
                ('country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('opening_date', models.DateField()),
                ('running_time', models.IntegerField()),
                ('screening', models.BooleanField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.director')),
            ],
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name',
        ),
        migrations.AddField(
            model_name='genre',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.genre'),
        ),
    ]
