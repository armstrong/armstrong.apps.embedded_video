# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EmbeddedVideo'
        db.create_table('embedded_video_embeddedvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('pub_status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('authors_extra', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('authors_override', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('video', self.gf('armstrong.core.arm_content.fields.video.EmbeddedVideoField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('aspect_ratio', self.gf('django.db.models.fields.CharField')(default='16:9', max_length=5)),
            ('screencap_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('embedded_video', ['EmbeddedVideo'])

        # Adding M2M table for field authors on 'EmbeddedVideo'
        db.create_table('embedded_video_embeddedvideo_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('embeddedvideo', models.ForeignKey(orm['embedded_video.embeddedvideo'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('embedded_video_embeddedvideo_authors', ['embeddedvideo_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting model 'EmbeddedVideo'
        db.delete_table('embedded_video_embeddedvideo')

        # Removing M2M table for field authors on 'EmbeddedVideo'
        db.delete_table('embedded_video_embeddedvideo_authors')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'embedded_video.embeddedvideo': {
            'Meta': {'object_name': 'EmbeddedVideo'},
            'aspect_ratio': ('django.db.models.fields.CharField', [], {'default': "'16:9'", 'max_length': '5'}),
            'authors': ('armstrong.core.arm_content.fields.authors.AuthorsField', [], {'to': "orm['auth.User']", 'override_field_name': "'authors_override'", 'extra_field_name': "'authors_extra'", 'symmetrical': 'False'}),
            'authors_extra': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'authors_override': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'pub_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'screencap_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video': ('armstrong.core.arm_content.fields.video.EmbeddedVideoField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['embedded_video']
