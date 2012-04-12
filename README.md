# [Revolver][]

[![BuildStatus](https://secure.travis-ci.org/michaelcontento/revolver.png?branch=master)](http://travis-ci.org/michaelcontento/revolver)

## About

*TL;DR Wrapper for [Fabric][] and [Cuisine][] to achieve a clean, simple and
fun to use interface amplified with new high-level functions to quickly 
orchestrate your servers.*

***

Let me introduce you two other awesome tools / libraries, before I try to 
explain the gap [Revolver][] tries to fill. First there is [Fabric][], a very 
small and low-level wrapper around SSH written in [Python][]. It allows you to 
store a small *fabfile.py* next to your project, where you can define all the 
steps required to automate something via SSH on one to multiple servers (e.g. 
install and configure your software stack, deploy new versions, ...). 

But [Fabric][] is *really* low-level and there is a lack of fun. That's the 
point where [Cuisine][] joins the ring, because it's a collection of useful 
methods which really increases your amount of fun and pleasure. Unfortunately 
with some small, but really annoying, differences that are sometimes even 
incompatible. Some examples? 

    # Fabric
    run('apt-get install XYZ', use_sudo=True)

    # Cuisine
    with mode_sudo():
        run('apt-get install XYZ')

I really enjoy the contextmanager for running a block as superuser! But 
[Cuisine][] didn't patch all commands provided by [Fabric][] (`run()` in the 
example is patched but other commands, like `put()`, aren't and you'll run into 
strange / annoying errors). 

There is also a different scheme of naming things. [Fabric][] tends to use short 
function names inside clean namespaces (e.g `fabric.contrib.files.append`). 
But the API of [Cuisine][], on the other hand, follows `<object>_<operation>`
(e.g. `cuisine.file_append`). 

Both ways are reasonable and I don't wanna blame someone! Don't get me wrong!
I simply want a "cleaner" or "more compatible" API which I can extend with my
own new functions and keep the level of fun and pleasure high (at least for
me). And the last sentence is a short / good description of what [Revolver][] 
is about. Just a "unification" wrapper for [Fabric][] and [Cuisine][] with some 
new batteries included.

## Getting started

This project is currently not published to the official python package 
repository but it should be easy to get everything running:

    sudo easy_install https://github.com/michaelcontento/revolver/tarball/master

Or use the new alternate installer [Pip][]:

    sudo pip install https://github.com/michaelcontento/revolver/tarball/master#egg=revolver

Now [Revolver][] is installed and ready to use. But I would suggest to 
first read the documentation from [Fabric][] to get used with the whole 
workflow / principle. After that it should be easy for you to dig into the 
code, discover everything and write your first own `fabfile.py`. 

## Example

But for those who want to see fast results, here is a small example 
`fabfile.py`.

    # -*- coding: utf-8 -*-

    from revolver import user
    from revolver import contextmanager as ctx
    from revolver.project import Deployinator
    from revolver.core import env
    from revolver.tool import php
    from revolver.tool import ruby

    env.hosts = ['user@example.com']

    def setup():
        php.install(version='5.3.9')
        ruby.ensure(version='1.9.2-p290')
        user.ensure('own-user', home='/var/own-user')

    def deploy():
        with ctx.sudo(username='own-user'):
            dp = Deployinator()
            dp.run()

## Contributing

* Fork this project
* Make your changes (new features, bugfixes, examples, ...)
* Write tests for it 
* Be sure that *all other* tests are still green
* Send me a pull request

Too complicated? You just wanna mess around for yourself? Thats fine! Just 
skip everything after step two :)

## License

    Copyright 2009-2012 Michael Contento <michaelcontento@gmail.com>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

  [Pip]: http://www.pip-installer.org
  [Cuisine]: https://github.com/sebastien/cuisine
  [Fabric]: https://github.com/fabric/fabric
  [Python]: http://python.org
  [Revolver]: https://github.com/michaelcontento/revolver
