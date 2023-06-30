# Overlord library
from . import API
from core.models import Users
from core.library import api

API.path(
  "create",
  lambda req, *args, **kwargs: Users.create(**api.get_json(req)),
  "Create New User"
)

API.path(
  "login",
  lambda req, *args, **kwargs: Users.login(**api.get_json(req)),
  "Returns session data for an email/password combination"
)

API.path(
  "delete",
  lambda req, *args, **kwargs: Users.delete(**api.get_json(req)),
  "Deletes all data related to a specific uuid or email identifier"
)

API.path(
  "edit/password",
  lambda req, *args, **kwargs: Users.change_password(**api.get_json(req)),
  "Verifies the current user password and updates it to a new one"
)

API.path(
  "edit/email",
  lambda req, *args, **kwargs: Users.change_email(**api.get_json(req)),
  "Updates the users email to a new one"
)
