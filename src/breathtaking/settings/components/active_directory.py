import os

from django_auth_ldap.config import GroupOfNamesType, LDAPSearch, LDAPSearchUnion
import ldap


AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django_remote_auth_ldap.backend.RemoteUserLDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Baseline LDAP configuration.
AUTH_LDAP_SERVER_URI = os.getenv('AUTH_LDAP_SERVER_URI', "ldap://DC-1.COMPANY.ru")
AUTH_LDAP_AUTHORIZE_ALL_USERS = True
AUTH_LDAP_PERMIT_EMPTY_PASSWORD = True

AUTH_LDAP_BIND_DN = os.getenv('AUTH_LDAP_BIND_DN', "cn=svc-apache,cn=Users,dc=company,dc=ru")
AUTH_LDAP_BIND_PASSWORD = os.getenv('AUTH_LDAP_BIND_PASSWORD', "P@ssw0rd")

AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
        LDAPSearch("ou=Django,dc=company,dc=ru", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
        LDAPSearch("cn=Users,dc=company,dc=ru", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
)

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Groups,ou=Django,dc=company,dc=ru",
    ldap.SCOPE_SUBTREE, "(objectClass=group)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = "cn=active,ou=Groups,ou=Django,dc=company,dc=ru"

# ему будет отказано в аутентификации
AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=Groups,ou=Django,dc=company,dc=ru"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}
AUTH_LDAP_PROFILE_ATTR_MAP = {
    "employee_number": "employeeNumber"
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active,ou=Groups,ou=Django,dc=company,dc=ru",
    "is_staff": "cn=staff,ou=Groups,ou=Django,dc=company,dc=ru",
    "is_superuser": "cn=superuser,ou=Groups,ou=Django,dc=company,dc=ru"
}

AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
    "is_awesome": "cn=awesome,ou=Groups,ou=Django,dc=company,dc=ru",
}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
