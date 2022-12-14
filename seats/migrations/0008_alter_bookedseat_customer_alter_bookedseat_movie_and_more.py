# Generated by Django 4.1 on 2022-08-16 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
        ('seats', '0007_remove_seat_customer_bookedseat_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedseat',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookedseat',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmovie', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='bookedseat',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='seats.seat'),
        ),
    ]
