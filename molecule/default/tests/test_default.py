import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mariadb_installed(host):
    mariadb = host.package('MariaDB-server')
    assert mariadb.is_installed

    version = tuple(map(int, mariadb.version.split('-')[0].split('.')))
    version_error = "MariaDB version must be at least 10.1.23 or 10.2.7"
    assert version[0] >= 10, version_error
    assert version[1] >= 1, version_error
    if version[1] == 1:
        assert version[2] >= 23, version_error
    if version[1] == 2:
        assert version[2] >= 7, version_error


def test_mariadb_running(host):
    mariadb = host.service('mysql')
    assert mariadb.is_running
    assert mariadb.is_enabled


def test_mariabackup_installed(host):
    mariabackup = host.package('MariaDB-backup')
    assert mariabackup.is_installed


def test_user_mariabackup_exists(host):
    mariabackup = host.user('mariabackup')
    assert mariabackup.exists
