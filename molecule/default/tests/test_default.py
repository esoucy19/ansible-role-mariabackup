import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mariadb_installed(host):
    p = host.package('MariaDB-server')
    assert p.is_installed

    version = tuple(map(int, p.version.split('-')[0].split('.')))
    version_error = "MariaDB version must be at least 10.1.23 or 10.2.7"
    assert version[0] >= 10, version_error
    assert version[1] >= 1, version_error
    if version[1] == 1:
        assert version[2] >= 23, version_error
    if version[1] == 2:
        assert version[2] >= 7, version_error


def test_mariadb_running(host):
    s = host.service('mysql')
    assert s.is_running
    assert s.is_enabled


def test_mariabackup_installed(host):
    p = host.package('MariaDB-backup')
    assert p.is_installed
