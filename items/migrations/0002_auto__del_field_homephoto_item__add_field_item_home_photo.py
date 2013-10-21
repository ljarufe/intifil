# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HomePhoto.item'
        db.delete_column(u'items_homephoto', 'item_id')

        # Adding field 'Item.home_photo'
        db.add_column(u'items_item', 'home_photo',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['items.HomePhoto'], unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'HomePhoto.item'
        db.add_column(u'items_homephoto', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['items.Item']),
                      keep_default=False)

        # Deleting field 'Item.home_photo'
        db.delete_column(u'items_item', 'home_photo_id')


    models = {
        u'items.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'items.homephoto': {
            'Meta': {'object_name': 'HomePhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'shape': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'items.item': {
            'Meta': {'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'home_photo': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['items.HomePhoto']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'items.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'items.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['items']