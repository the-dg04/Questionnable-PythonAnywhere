# Generated by Django 3.1 on 2020-09-02 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Qapp', '0009_auto_20200831_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Qapp.accounts'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ques',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Qapp.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='Qdesc',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
