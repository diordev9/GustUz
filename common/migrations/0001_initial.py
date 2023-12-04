# Generated by Django 4.2.7 on 2023-12-03 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(max_length=255)),
                ('lng', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField()),
                ('metro', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to='files/')),
                ('type', models.CharField(choices=[('document', 'Document'), ('certificate', 'Certificate'), ('project', 'Project')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='common.region')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('web_site', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.ManyToManyField(blank=True, related_name='companies', to='common.address')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address', to='common.district'),
        ),
    ]