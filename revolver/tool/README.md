## About

## Basic API

All of these packages fulfill (but are not limited to) the following simple
interface:

- `install` will install or update the package
- `ensure` does nothing if the package is already installed

Some simple examples of this:

    from revolver.tool import nginx

    # Will always install or update to the latest version of nginx
    nginx.install()

    # Does nothing if the command 'nginx' is available
    nginx.ensure()

But often you need to specify a desired version, which cause a slightly changed
behaviour:

    from revolver.tool import python

    # Will always install (read: recompile) python 2.7.2
    python.install('2.7.2')

    # Does nothing if python 2.7.2 is already there
    python.ensure('2.7.2')

## Bound to the user

The following tools are installed into the currently selected user:

- `awsenv`
- `nodejs`, `nodejs_nvm`
- `php`, `php_build` and `php_phpenv`
- `python` and `pythonbrew`
- `ruby`, `ruby_build` and `ruby_rbenv`

As you might noticed: most of this are programming languages. And that for a
good reason. Most of the time you simply *don't* want to change the used version
of python (as an example) for the whole system. Deploying an application build
with nodejs? You already have a dedicated user? Fine. Just install the required
version of nodejs into the users "scope" and your done. This allows you to use
multiple versions of nodejs on one system. Following a small example:

    from revolver import contextmanager as ctx
    from revolver import user
    from revolver.tool import nodejs

    user.create("application")
    with ctx.sudo("application"):
        nodejs.install("0.6.14")
