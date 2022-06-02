"""CILogon OAuthAuthenticator for JupyterHub

Uses OAuth 2.0 with cilogon.org (override with CILOGON_HOST)

Caveats:

- For allowed user list /admin purposes, username will be the ePPN by default.
  This is typically an email address and may not work as a Unix userid.
  Normalization may be required to turn the JupyterHub username into a Unix username.
- Default username_claim of ePPN does not work for all providers,
  e.g. generic OAuth such as Google.
  Use `c.CILogonOAuthenticator.username_claim = 'email'` to use
  email instead of ePPN as the JupyterHub username.
"""
from jupyterhub.auth import LocalAuthenticator
from .oauth2 import OAuthenticator


class CILogonOAuthenticator(OAuthenticator):
    pass


class LocalCILogonOAuthenticator(LocalAuthenticator, CILogonOAuthenticator):

    """A version that mixes in local system user creation"""

    pass
