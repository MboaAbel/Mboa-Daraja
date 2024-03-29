# Generated by Django 3.0.5 on 2023-10-31 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FX_Profile', '0002_auto_20231030_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='image01',
            field=models.ImageField(default='img/Mboa Academy.jpg', upload_to='products_img'),
        ),
        migrations.AddField(
            model_name='item',
            name='image02',
            field=models.ImageField(default='img/Mboa Academy.jpg', upload_to='products_img'),
        ),
        migrations.AddField(
            model_name='item',
            name='image03',
            field=models.ImageField(default='img/Mboa Academy.jpg', upload_to='products_img'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image03',
            field=models.ImageField(default='img/Mboa Academy.jpg', upload_to='profile_img'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='img/Mboa Academy.jpg', upload_to='products_img'),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=50, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FX_Profile.Product')),
            ],
        ),
    ]
