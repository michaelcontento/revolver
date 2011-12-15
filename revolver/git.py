# -*- coding: utf-8 -*-

import os

from revolver import directory as dir
from revolver.core import local

def repository_name():
    command = "grep 'url' .git/config | cut -d':' -f2"
    return local(command, capture=True)

def create_archive(revision):
    tmp_folder = dir.temp_local()
    tmp_tar = os.path.join(tmp_folder, 'repo.tar.gz')

    local(
        'git archive --format=tar %(rev)s | gzip > %(tar)s' 
        % {'rev': revision, 'tar': tmp_tar}
    )

    return tmp_tar

def revparse(revision):
    return local('git rev-parse %s' % revision, capture=True)
