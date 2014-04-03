Title: puppet to automate pelican environment
Date:  2014-03-22 22:00

So everything started when I was working in a personal project written in jruby, and one day I've read about pelican and how to host it in github. So I thought maybe writting a blog can be fun with this.

The first problem I have was that I have to setup python and all the things related ( virtualenv/ pip/ pelican/ Markdown) and how this gets messy when I start to have a lot of things installed in my machine. So I wanted to keep my machine in a good shape minimizing the packages installed and do it only once in a while.

I was already interested in automation, at work we have a few conversation with the DevOps team to see how we could automate our dev environments, so I heard of puppet. It looks like a good opportunity to learn it.

So I got my hands dirty.

First, I installed puppet, probably the only thing needed along with git which could be installed by puppet but I want to have a repository for the puppet manifest, so I can keep it updated.

Here is the manifest:
  
    class pelican{
      $user = "youruser"
      $pelican_virtualenvs = "/home/${user}/workspace/virtualenvs/pelican"
      $folders = ["/home/${user}/workspace", "/home/${user}/workspace/virtualenvs",$pelican_virtualenvs]
      $pathRepo = "${pelican_virtualenvs}/source"
      $gitRepo = "git://github.com/yourgituser/blog"

      user {$user:
        ensure => present,
      }

      file {$folders:
        ensure => directory,
        owner => $user
      }

      python::virtualenv {$pelican_virtualenvs:
        owner => $user,
        systempkgs   => true,
        notify => Exec['activate_virtualenv_pelican'],
      }
      ->
      exec { 'activate_virtualenv_pelican':
        command => "bash -c 'source ${pelican_virtualenvs}/bin/activate'",
        path => "/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin",
      }
      
      python::pip {'install_pelican':
        pkgname => 'pelican',
        virtualenv => "/home/${user}/workspace/virtualenvs/pelican",
        owner => $user,
        require => Exec['activate_virtualenv_pelican']
      }
      
      python::pip {'install_markdown':
        pkgname => 'Markdown',
        virtualenv => "/home/${user}/workspace/virtualenvs/pelican",
        owner => $user,
        require => Exec['activate_virtualenv_pelican']
      }
       
      python::pip {'install_fabric':
        pkgname => 'Fabric',
        virtualenv => "/home/${user}/workspace/virtualenvs/pelican",
        owner => $user,
        require => Exec['activate_virtualenv_pelican']
      }

      python::pip {'install_ghp_import':
        pkgname => 'ghp-import',
        virtualenv => "/home/${user}/workspace/virtualenvs/pelican",
        owner => $user,
        require => Exec['activate_virtualenv_pelican']
      }

      vcsrepo { $pathRepo:
        ensure => present,
        provider => git,
        source => $gitRepo,
        revision => 'master',
        user => $user,
        require => Exec['activate_virtualenv_pelican'],
      }
    } 

Disclaimer: Probably there are ways to do it better but for me this way was easier. Let me know if you know a better way  


