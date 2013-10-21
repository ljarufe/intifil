# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'global_presence_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address_line_3', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='team_name', unique_with=())),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='global_presence_item_set', null=True, to=orm['items.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('flag_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'global_presence', ['Item'])

        # Adding model 'Country'
        db.create_table(u'global_presence_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='name', unique_with=())),
            ('flag_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['global_presence.Item'])),
        ))
        db.send_create_signal(u'global_presence', ['Country'])

        # Adding model 'Team'
        db.create_table(u'global_presence_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address_line_3', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='name', unique_with=())),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('address_line_4', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['global_presence.Country'])),
        ))
        db.send_create_signal(u'global_presence', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'global_presence_item')

        # Deleting model 'Country'
        db.delete_table(u'global_presence_country')

        # Deleting model 'Team'
        db.delete_table(u'global_presence_team')


    models = {
        u'global_presence.country': {
            'Meta': {'object_name': 'Country'},
            'flag_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['global_presence.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'global_presence.item': {
            'Meta': {'object_name': 'Item'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_line_3': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'global_presence_item_set'", 'null': 'True', 'to': u"orm['items.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'flag_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'team_name'", 'unique_with': '()'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'global_presence.team': {
            'Meta': {'ordering': "['id']", 'object_name': 'Team'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_line_3': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_line_4': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['global_presence.Country']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'items.category': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['global_presence']