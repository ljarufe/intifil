# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TeamMember.photo'
        db.alter_column(u'enterprise_teammember', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'TeamMember.description'
        db.alter_column(u'enterprise_teammember', 'description', self.gf('tinymce.models.HTMLField')())
        # Deleting field 'Enterprise.slogan'
        db.delete_column(u'enterprise_enterprise', 'slogan')

        # Deleting field 'Enterprise.message'
        db.delete_column(u'enterprise_enterprise', 'message')


    def backwards(self, orm):

        # Changing field 'TeamMember.photo'
        db.alter_column(u'enterprise_teammember', 'photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'TeamMember.description'
        db.alter_column(u'enterprise_teammember', 'description', self.gf('django.db.models.fields.TextField')())
        # Adding field 'Enterprise.slogan'
        db.add_column(u'enterprise_enterprise', 'slogan',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Enterprise.message'
        db.add_column(u'enterprise_enterprise', 'message',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250),
                      keep_default=False)


    models = {
        u'enterprise.enterprise': {
            'Meta': {'object_name': 'Enterprise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'enterprise.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['enterprise']