from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

content_type = ContentType.objects.get_for_model(Book)

add_perm = Permission.objects.get(codename='can_add_book', content_type=content_type)
change_perm = Permission.objects.get(codename='can_change_book', content_type=content_type)
delete_perm = Permission.objects.get(codename='can_delete_book', content_type=content_type)

group = Group.objects.get(name='Librarian')
group.permissions.add(add_perm, change_perm, delete_perm)
