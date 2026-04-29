from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("festival", "0008_alter_dia_cor"),
    ]

    operations = [
        migrations.AddField(
            model_name="palco",
            name="acessibilidade_mobilidade_reduzida",
            field=models.BooleanField(default=False),
        ),
    ]
