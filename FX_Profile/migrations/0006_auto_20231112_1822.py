# Generated by Django 3.0.5 on 2023-11-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FX_Profile', '0005_followerscount_likepost_member_post_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
