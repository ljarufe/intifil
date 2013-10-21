# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Photo.order'
        db.alter_column(u'items_photo', 'order', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True))
        # Adding unique constraint on 'Photo', fields ['order']
        db.create_unique(u'items_photo', ['order'])


        # Changing field 'Video.order'
        db.alter_column(u'items_video', 'order', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True))
        # Adding unique constraint on 'Video', fields ['order']
        db.create_unique(u'items_video', ['order'])


        # Changing field 'Item.description'
        db.alter_column(u'items_item', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Item.order'
        db.alter_column(u'items_item', 'order', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Removing unique constraint on 'Video', fields ['order']
        db.delete_unique(u'items_video', ['order'])

        # Removing unique constraint on 'Photo', fields ['order']
        db.delete_unique(u'items_photo', ['order'])


        # Changing field 'Photo.order'
        db.alter_column(u'items_photo', 'order', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Video.order'
        db.alter_column(u'items_video', 'order', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Item.description'
        db.alter_column(u'items_item', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Item.order'
        db.alter_column(u'items_item', 'order', self.gf('django.db.models.fields.IntegerField')(default=None))

    models = {
        u'items.category': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'items.homephoto': {
            'Meta': {'object_name': 'HomePhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'shape': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'items.item': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Category']"}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'home_photo': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['items.HomePhoto']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'items.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'items.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['items']