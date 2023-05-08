# Generated by Django 4.2 on 2023-05-07 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=50)),
                ('Images', models.ImageField(blank=True, upload_to='photos/Image')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ImageView.category')),
            ],
        ),
    ]
