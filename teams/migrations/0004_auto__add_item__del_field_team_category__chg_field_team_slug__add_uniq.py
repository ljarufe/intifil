# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'teams_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='name', unique_with=())),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_item_set', null=True, to=orm['items.Category'])),
        ))
        db.send_create_signal(u'teams', ['Item'])

        # Deleting field 'Team.category'
        db.delete_column(u'teams_team', 'category_id')


        # Changing field 'Team.slug'
        db.alter_column(u'teams_team', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='name', unique_with=()))
        # Adding unique constraint on 'Team', fields ['slug']
        db.create_unique(u'teams_team', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Team', fields ['slug']
        db.delete_unique(u'teams_team', ['slug'])

        # Deleting model 'Item'
        db.delete_table(u'teams_item')

        # Adding field 'Team.category'
        db.add_column(u'teams_team', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_team_set', null=True, to=orm['items.Category'], blank=True),
                      keep_default=False)


        # Changing field 'Team.slug'
        db.alter_column(u'teams_team', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        u'items.category': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'teams.item': {
            'Meta': {'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_item_set'", 'null': 'True', 'to': u"orm['items.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'teams.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mini_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'teams.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Team']"})
        }
    }

    complete_apps = ['teams']