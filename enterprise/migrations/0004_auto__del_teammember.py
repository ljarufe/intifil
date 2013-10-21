# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TeamMember'
        db.delete_table(u'enterprise_teammember')


    def backwards(self, orm):
        # Adding model 'TeamMember'
        db.create_table(u'enterprise_teammember', (
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'enterprise', ['TeamMember'])


    models = {
        u'enterprise.enterprise': {
            'Meta': {'object_name': 'Enterprise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['enterprise']