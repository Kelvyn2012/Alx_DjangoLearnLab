# app/management/commands/setup_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps


class Command(BaseCommand):
    help = "Create user groups and assign permissions"

    def handle(self, *args, **kwargs):
        article_model = apps.get_model("bookshelf", "Article")

        permissions = {
            "can_view": Permission.objects.get(codename="can_view"),
            "can_create": Permission.objects.get(codename="can_create"),
            "can_edit": Permission.objects.get(codename="can_edit"),
            "can_delete": Permission.objects.get(codename="can_delete"),
        }

        # Viewers
        viewers, created = Group.objects.get_or_create(name="Viewers")
        viewers.permissions.set([permissions["can_view"]])

        # Editors
        editors, created = Group.objects.get_or_create(name="Editors")
        editors.permissions.set(
            [
                permissions["can_view"],
                permissions["can_create"],
                permissions["can_edit"],
            ]
        )

        # Admins
        admins, created = Group.objects.get_or_create(name="Admins")
        admins.permissions.set(permissions.values())

        self.stdout.write(
            self.style.SUCCESS("Groups and permissions set up successfully")
        )
