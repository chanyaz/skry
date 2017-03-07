# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150513_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='alternate_template',
            field=models.ForeignKey(blank=True, help_text='Optional alternate template to use for this story.', null=True, on_delete=django.db.models.deletion.CASCADE, to='display.Template'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(help_text='Forms part of the URL for this story.', max_length=128),
        ),
        migrations.AlterField(
            model_name='story',
            name='alternate_template',
            field=models.ForeignKey(blank=True, help_text='Optional alternate template to use for this story.', null=True, on_delete=django.db.models.deletion.CASCADE, to='display.Template'),
        ),
        migrations.AlterField(
            model_name='story',
            name='assignment_slug',
            field=models.CharField(help_text='Succinct, quasi-unique identifier for this story. Should NOT contain a date, section, or any other information already stored on another story field.', max_length=64),
        ),
        migrations.AlterField(
            model_name='story',
            name='breaking_duration',
            field=models.PositiveSmallIntegerField(default=0, help_text='How long the story should be displayed as breaking news.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='card',
            field=models.ForeignKey(blank=True, help_text='Image to display with this story in a story list view.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_story_card', to='attachments.Image'),
        ),
        migrations.AlterField(
            model_name='story',
            name='card_focus',
            field=models.CharField(choices=[('cc', 'center center'), ('cl', 'center left'), ('cr', 'center right'), ('tl', 'top left'), ('tc', 'top center'), ('tr', 'top right'), ('bl', 'bottom left'), ('bc', 'bottom center'), ('br', 'bottom right')], default='cc', help_text='Location of the focal point of the card image.', max_length=2),
        ),
        migrations.AlterField(
            model_name='story',
            name='card_size',
            field=models.ForeignKey(help_text='The aspect ratio in which the card should be displayed.', on_delete=django.db.models.deletion.CASCADE, to='display.CardSize'),
        ),
        migrations.AlterField(
            model_name='story',
            name='feature_card_image',
            field=models.BooleanField(default=True, help_text="Whether or not the card image should also be displayed as the story's featured image."),
        ),
        migrations.AlterField(
            model_name='story',
            name='featured_audio',
            field=models.ForeignKey(blank=True, help_text='The most prominent audio associated with this story.', null=True, on_delete=django.db.models.deletion.CASCADE, to='attachments.Audio'),
        ),
        migrations.AlterField(
            model_name='story',
            name='featured_image',
            field=models.ForeignKey(blank=True, help_text='The most prominent image associated with this story.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core_story_featured_image', to='attachments.Image'),
        ),
        migrations.AlterField(
            model_name='story',
            name='featured_video',
            field=models.ForeignKey(blank=True, help_text='The most prominent video associated with this story.', null=True, on_delete=django.db.models.deletion.CASCADE, to='attachments.Video'),
        ),
        migrations.AlterField(
            model_name='story',
            name='game',
            field=models.ForeignKey(blank=True, help_text='Sports game associated with this story.', null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.Game'),
        ),
        migrations.AlterField(
            model_name='story',
            name='late_run',
            field=models.BooleanField(default=False, help_text='Whether or not the story is planned to come in later than stories in the section typically do.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='position',
            field=models.PositiveIntegerField(db_index=True, help_text='How this story is ordered relative to other stories.', unique=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='status',
            field=models.ForeignKey(help_text='Current state in workflow.', on_delete=django.db.models.deletion.CASCADE, to='core.Status'),
        ),
        migrations.AlterField(
            model_name='story',
            name='subhead',
            field=models.CharField(blank=True, help_text='Addtional title that suplements the primary title.', max_length=128),
        ),
        migrations.AlterField(
            model_name='story',
            name='teaser',
            field=models.CharField(blank=True, help_text='Short subtext related to the story to encourage readers to read the story.', max_length=128),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(blank=True, help_text='Publicly displayed headline.', max_length=128),
        ),
        migrations.AlterField(
            model_name='story',
            name='url_slug',
            field=models.SlugField(blank=True, help_text='Forms a part of the URL for this story.', max_length=128),
        ),
    ]