# Generated by Django 4.2.5 on 2023-09-29 12:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_budgets', to=settings.AUTH_USER_MODEL),
        ),
    ]
