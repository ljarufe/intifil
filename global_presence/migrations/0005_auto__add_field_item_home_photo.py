# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.home_photo'
        db.add_column(u'global_presence_item', 'home_photo',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='global_presence_item_set', unique=True, null=True, to=orm['items.HomePhoto']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.home_photo'
        db.delete_column(u'global_presence_item', 'home_photo_id')


    models = {
        u'global_presence.country': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Country'},
            'flag_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['global_presence.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'global_presence.item': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Item'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_line_3': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'global_presence_item_set'", 'null': 'True', 'to': u"orm['items.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'flag_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'home_photo': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'global_presence_item_set'", 'unique': 'True', 'null': 'True', 'to': u"orm['items.HomePhoto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'show_sub_pages_on_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'items.homephoto': {
            'Meta': {'object_name': 'HomePhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'shape': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['global_presence']