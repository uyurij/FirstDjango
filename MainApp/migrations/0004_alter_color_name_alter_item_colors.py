from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_color_item_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='item',
            name='colors',
            field=models.ManyToManyField(default='', to='MainApp.color'),
        ),
    ]
