"""
Transactional version control for Django models.

Developed by Dave Hall.

<http://www.etianen.com/>
"""

from reversion.revisions import default_revision_manager, revision_context_manager, VersionAdapter
from reversion.admin import VersionAdmin


# Legacy revision reference.
revision = default_revision_manager  # TODO: Depricate eventually.


# Easy registration methods.
register = default_revision_manager.register
is_registered = default_revision_manager.is_registered
unregister = default_revision_manager.unregister
get_adapter = default_revision_manager.get_adapter
get_registered_models = default_revision_manager.get_registered_models


# Context management.
create_revision = revision_context_manager.create_revision
context = revision_context_manager.context

    
# Revision meta data.
get_user = revision_context_manager.get_user
set_user = revision_context_manager.set_user
get_comment = revision_context_manager.get_comment
set_comment = revision_context_manager.set_comment
add_meta = revision_context_manager.add_meta
get_ignore_duplicates = revision_context_manager.get_ignore_duplicates
set_ignore_duplicates = revision_context_manager.set_ignore_duplicates


# Low level API.
get_for_object_reference = default_revision_manager.get_for_object_reference
get_for_object = default_revision_manager.get_for_object
get_unique_for_object = default_revision_manager.get_unique_for_object
get_for_date = default_revision_manager.get_for_date
get_deleted = default_revision_manager.get_deleted


# TODO: Test multi table inheritance.
# TODO: Test meta
# TODO: Test fields and exclude params.