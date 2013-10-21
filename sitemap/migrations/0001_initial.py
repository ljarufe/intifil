# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Column'
        db.create_table(u'sitemap_column', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('include_intranet_link', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('include_sitemap_link', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sitemap', ['Column'])

        # Adding model 'ColumnCategory'
        db.create_table(u'sitemap_columncategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.Category'])),
            ('column', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sitemap.Column'])),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'sitemap', ['ColumnCategory'])


    def backwards(self, orm):
        # Deleting model 'Column'
        db.delete_table(u'sitemap_column')

        # Deleting model 'ColumnCategory'
        db.delete_table(u'sitemap_columncategory')


    models = {
        u'items.category': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'sitemap.column': {
            'Meta': {'object_name': 'Column'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.Category']", 'through': u"orm['sitemap.ColumnCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_intranet_link': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'include_sitemap_link': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'sitemap.columncategory': {
            'Meta': {'object_name': 'ColumnCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.Category']"}),
            'column': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sitemap.Column']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['sitemap']