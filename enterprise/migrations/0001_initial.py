# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Enterprise'
        db.create_table(u'enterprise_enterprise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'enterprise', ['Enterprise'])

        # Adding model 'TeamMember'
        db.create_table(u'enterprise_teammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'enterprise', ['TeamMember'])


    def backwards(self, orm):
        # Deleting model 'Enterprise'
        db.delete_table(u'enterprise_enterprise')

        # Deleting model 'TeamMember'
        db.delete_table(u'enterprise_teammember')


    models = {
        u'enterprise.enterprise': {
            'Meta': {'object_name': 'Enterprise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'enterprise.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['enterprise']