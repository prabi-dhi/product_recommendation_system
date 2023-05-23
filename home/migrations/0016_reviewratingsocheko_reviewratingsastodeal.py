# Generated by Django 4.1.5 on 2023-01-28 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_reviewratingdaraz'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRatingSocheko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=100, null=True)),
                ('rating', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.socheko_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRatingSastodeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=100, null=True)),
                ('rating', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sastodeal_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
