from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("festival", "0004_palco_capacidade"),
    ]

    operations = [
        migrations.AddField(
            model_name="palco",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="palcos/"),
        ),
    ]
