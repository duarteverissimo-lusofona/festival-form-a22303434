from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("festival", "0003_palco_alter_concerto_banda_alter_concerto_dia_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="palco",
            name="capacidade",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
