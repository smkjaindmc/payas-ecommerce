# Generated by Django 2.1.4 on 2019-09-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0005_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
