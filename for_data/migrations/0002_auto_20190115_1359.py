# Generated by Django 2.1.5 on 2019-01-15 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('for_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_verse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_from_verse', to='for_data.Verse')),
            ],
        ),
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='for_data.LinkType'),
        ),
        migrations.AddField(
            model_name='link',
            name='to_verse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_to_verse', to='for_data.Verse'),
        ),
    ]
