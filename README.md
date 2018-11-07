
[![Build Status](https://travis-ci.org/esoucy19/ansible-role-mariabackup.svg?branch=master)](https://travis-ci.org/esoucy19/ansible-role-mariabackup)

Ansible Role: mariabackup
=========================

This role installs and configures the MariaDB backup software Mariabackup on
RedHat-based distributions. The role's responsibilities are to:

- Install Mariabackup.
- Create a system account with proper permissions to run backups under.
- Create a .my.cnf file with credentials in the system user's home directory.
- Create a database account with proper permissions to run backups under.

Requirements
------------

Mariabackup requires the MariaDB version to be at least 10.1.23 or 10.2.7. Any
version 10.3 and up will also do.

This role requires that MariaDB be already installed, and that mariabackup be
available in the system's repositories.

See [bertvv.mariadb](https://galaxy.ansible.com/bertvv/mariadb) for a role to
setup the repositories and install MariaDB.

Role Variables
--------------

Here are the variables used with their default values

```yaml
- mariabackup_user: "mariabackup" # The system user that backups will run under.
- mariabackup_mysql_user: "mariabackup" # The database user that backups will use.
- mariabackup_mysql_password: "" # The password for the database user.
- mariadb_root_password: "" # The root password the role will use to create the database user.
```

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: server
  roles:
      - role: esoucy19.mariabackup
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by [Etienne Soucy](https://gitlab.com/esoucy19).
