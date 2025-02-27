# Managing Permissions and Groups in Django

## Overview

This project implements Django's built-in permission system to manage user access. Permissions are assigned to groups, and views are protected based on these permissions.

## 1. Setting Up Permissions and Groups

Permissions are assigned to groups to control user access levels:

- **Editors** → Can edit content (`can_edit`)
- **Viewers** → Can only view content (`can_view`)
- **Admins** → Can edit, view, and delete content (`can_edit`, `can_view`, `can_delete`)

### Creating Groups and Assigning Permissions

You can create groups and assign permissions in the Djano Admin:

1. Go to the Django Admin interface.
2. Login as staff user
3. Add new groups
4. Add permissions for each of the groups i.e can_edit, can_delete, can_view

### Creating Groups and Assigning Permissions

You can create groups and assign permissions in the Django shell:

```python
from django.contrib.auth.models import Group, Permission

# Create groups
editors_group, _ = Group.objects.get_or_create(name="Editors")
viewers_group, _ = Group.objects.get_or_create(name="Viewers")
admins_group, _ = Group.objects.get_or_create(name="Admins")

# Assign permissions
editors_group.permissions.set(Permission.objects.filter(codename__in=["can_edit"]))
viewers_group.permissions.set(Permission.objects.filter(codename__in=["can_view"]))
admins_group.permissions.set(Permission.objects.filter(codename__in=["can_edit", "can_view", "can_delete"]))

```
