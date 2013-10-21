# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Video.name_en'
        db.add_column(u'items_video', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Video.name_it'
        db.add_column(u'items_video', 'name_it',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Video.name_zh'
        db.add_column(u'items_video', 'name_zh',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Video.name_ja'
        db.add_column(u'items_video', 'name_ja',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Video.url'
        db.alter_column(u'items_video', 'url', self.gf('embed_video.fields.EmbedVideoField')(max_length=200))
        # Adding field 'Item.name_en'
        db.add_column(u'items_item', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.name_it'
        db.add_column(u'items_item', 'name_it',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.name_zh'
        db.add_column(u'items_item', 'name_zh',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.name_ja'
        db.add_column(u'items_item', 'name_ja',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Photo.name_en'
        db.add_column(u'items_photo', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Photo.name_it'
        db.add_column(u'items_photo', 'name_it',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Photo.name_zh'
        db.add_column(u'items_photo', 'name_zh',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Photo.name_ja'
        db.add_column(u'items_photo', 'name_ja',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Photo', fields ['subitem', 'order']
        db.create_unique(u'items_photo', ['subitem_id', 'order'])

        # Adding field 'SubItem.name_en'
        db.add_column(u'items_subitem', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubItem.name_it'
        db.add_column(u'items_subitem', 'name_it',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubItem.name_zh'
        db.add_column(u'items_subitem', 'name_zh',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubItem.name_ja'
        db.add_column(u'items_subitem', 'name_ja',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubItem.description_en'
        db.add_column(u'items_subitem', 'description_en',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubItem.description_it'
        db.add_column(u'items_subitem', 'description_it',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubItem.description_zh'
        db.add_column(u'items_subitem', 'description_zh',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SubItem.description_ja'
        db.add_column(u'items_subitem', 'description_ja',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'SubItem', fields ['item', 'order']
        db.create_unique(u'items_subitem', ['item_id', 'order'])

        # Adding field 'Category.name_en'
        db.add_column(u'items_category', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.name_it'
        db.add_column(u'items_category', 'name_it',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.name_zh'
        db.add_column(u'items_category', 'name_zh',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.name_ja'
        db.add_column(u'items_category', 'name_ja',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'SubItem', fields ['item', 'order']
        db.delete_unique(u'items_subitem', ['item_id', 'order'])

        # Removing unique constraint on 'Photo', fields ['subitem', 'order']
        db.delete_unique(u'items_photo', ['subitem_id', 'order'])

        # Deleting field 'Video.name_en'
        db.delete_column(u'items_video', 'name_en')

        # Deleting field 'Video.name_it'
        db.delete_column(u'items_video', 'name_it')

        # Deleting field 'Video.name_zh'
        db.delete_column(u'items_video', 'name_zh')

        # Deleting field 'Video.name_ja'
        db.delete_column(u'items_video', 'name_ja')


        # Changing field 'Video.url'
        db.alter_column(u'items_video', 'url', self.gf('django.db.models.fields.URLField')(max_length=200))
        # Deleting field 'Item.name_en'
        db.delete_column(u'items_item', 'name_en')

        # Deleting field 'Item.name_it'
        db.delete_column(u'items_item', 'name_it')

        # Deleting field 'Item.name_zh'
        db.delete_column(u'items_item', 'name_zh')

        # Deleting field 'Item.name_ja'
        db.delete_column(u'items_item', 'name_ja')

        # Deleting field 'Photo.name_en'
        db.delete_column(u'items_photo', 'name_en')

        # Deleting field 'Photo.name_it'
        db.delete_column(u'items_photo', 'name_it')

        # Deleting field 'Photo.name_zh'
        db.delete_column(u'items_photo', 'name_zh')

        # Deleting field 'Photo.name_ja'
        db.delete_column(u'items_photo', 'name_ja')

        # Deleting field 'SubItem.name_en'
        db.delete_column(u'items_subitem', 'name_en')

        # Deleting field 'SubItem.name_it'
        db.delete_column(u'items_subitem', 'name_it')

        # Deleting field 'SubItem.name_zh'
        db.delete_column(u'items_subitem', 'name_zh')

        # Deleting field 'SubItem.name_ja'
        db.delete_column(u'items_subitem', 'name_ja')

        # Deleting field 'SubItem.description_en'
        db.delete_column(u'items_subitem', 'description_en')

        # Deleting field 'SubItem.description_it'
        db.delete_column(u'items_subitem', 'description_it')

        # Deleting field 'SubItem.description_zh'
        db.delete_column(u'items_subitem', 'description_zh')

        # Deleting field 'SubItem.description_ja'
        db.delete_column(u'items_subitem', 'description_ja')

        # Deleting field 'Category.name_en'
        db.delete_column(u'items_category', 'name_en')

        # Deleting field 'Category.name_it'
        db.delete_column(u'items_category', 'name_it')

        # Deleting field 'Category.name_zh'
        db.delete_column(u'items_category', 'name_zh')

        # Deleting field 'Category.name_ja'
        db.delete_column(u'items_category', 'name_ja')


    models = {
        u'items.category': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_ja': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_ja': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'show_sub_pages_on_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'items.photo': {
            'Meta': {'ordering': "['order']", 'unique_together': "(('order', 'subitem'),)", 'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_ja': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'subitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.SubItem']", 'null': 'True'})
        },
        u'items.subitem': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('item', 'order'),)", 'object_name': 'SubItem'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'description_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_it': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_ja': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_zh': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_ja': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'items.video': {
            'Meta': {'ordering': "['order']", 'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_ja': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_zh': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'subitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.SubItem']", 'null': 'True'}),
            'url': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['items']