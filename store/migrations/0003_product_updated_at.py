# Generated by Django 4.1.3 on 2022-12-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_alter_category_options_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
