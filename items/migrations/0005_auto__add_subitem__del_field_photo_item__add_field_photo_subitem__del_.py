# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubItem'
        db.create_table(u'items_subitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.Item'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'items', ['SubItem'])

        # Deleting field 'Photo.item'
        db.delete_column(u'items_photo', 'item_id')

        # Adding field 'Photo.subitem'
        db.add_column(u'items_photo', 'subitem',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.SubItem'], null=True),
                      keep_default=False)

        # Deleting field 'Video.item'
        db.delete_column(u'items_video', 'item_id')

        # Adding field 'Video.subitem'
        db.add_column(u'items_video', 'subitem',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.SubItem'], null=True),
                      keep_default=False)

        # Deleting field 'Item.description'
        db.delete_column(u'items_item', 'description')


    def backwards(self, orm):
        # Deleting model 'SubItem'
        db.delete_table(u'items_subitem')

        # Adding field 'Photo.item'
        db.add_column(u'items_photo', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['items.Item']),
                      keep_default=False)

        # Deleting field 'Photo.subitem'
        db.delete_column(u'items_photo', 'subitem_id')

        # Adding field 'Video.item'
        db.add_column(u'items_video', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['items.Item']),
                      keep_default=False)

        # Deleting field 'Video.subitem'
        db.delete_column(u'items_video', 'subitem_id')

        # Adding field 'Item.description'
        db.add_column(u'items_item', 'description',
                      self.gf('tinymce.models.HTMLField')(default='', blank=True),
                      keep_default=False)


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'subitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.SubItem']", 'null': 'True'})
        },
        u'items.subitem': {
            'Meta': {'object_name': 'SubItem'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
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