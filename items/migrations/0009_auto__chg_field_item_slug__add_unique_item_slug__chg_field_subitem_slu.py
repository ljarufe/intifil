# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.slug'
        db.alter_column(u'items_item', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='name', unique_with=()))
        # Adding unique constraint on 'Item', fields ['slug']
        db.create_unique(u'items_item', ['slug'])


        # Changing field 'SubItem.slug'
        db.alter_column(u'items_subitem', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='name', unique_with=()))
        # Adding unique constraint on 'SubItem', fields ['slug']
        db.create_unique(u'items_subitem', ['slug'])


        # Changing field 'Category.slug'
        db.alter_column(u'items_category', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=255, populate_from='name', unique_with=()))
        # Adding unique constraint on 'Category', fields ['slug']
        db.create_unique(u'items_category', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Category', fields ['slug']
        db.delete_unique(u'items_category', ['slug'])

        # Removing unique constraint on 'SubItem', fields ['slug']
        db.delete_unique(u'items_subitem', ['slug'])

        # Removing unique constraint on 'Item', fields ['slug']
        db.delete_unique(u'items_item', ['slug'])


        # Changing field 'Item.slug'
        db.alter_column(u'items_item', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Changing field 'SubItem.slug'
        db.alter_column(u'items_subitem', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Changing field 'Category.slug'
        db.alter_column(u'items_category', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
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
        },
        u'items.item': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Category']"}),
            'home_photo': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['items.HomePhoto']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'items.photo': {
            'Meta': {'unique_together': "(('order', 'subitem'),)", 'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.SubItem']", 'null': 'True'})
        },
        u'items.subitem': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('item', 'order'),)", 'object_name': 'SubItem'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'items.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'subitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.SubItem']", 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['items']