# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import os

from revolver import directory as dir
from revolver import core

def repository_name():
    command = "grep 'url' .git/config | cut -d':' -f2"
    return core.local(command, capture=True)

def create_archive(revision):
    tmp_folder = dir.temp_local()
    tmp_tar = os.path.join(tmp_folder, 'repo.tar.gz')

    core.local(
        'git archive --format=tar %(rev)s | gzip > %(tar)s'
        % {'rev': revision, 'tar': tmp_tar}
    )

    return tmp_tar

def revparse(revision):
    return core.local('git rev-parse %s' % revision, capture=True)
