Title: puppet to automate pelican environment
Date:  2014-03-22 22:00

So everything started when I was working in a personal project written in jruby, and one day I've read about pelican and how to host it in github. So I thought maybe writting a blog can be fun with this.

The first problem I have was that I have to setup python and all the things related ( virtualenv/ pip/ pelican/ Markdown) and how this is get messy when I start to have a lot of things installed in my machine. So I wanted to keep my machine in a good shape minimizing the packages installed

I was already interested in automation, at work we have a few converstation with the DevOps team to see how we could automate our dev environments, so I heard of puppet and to me it looks like a good opportunity to learn it.

So I got my hands dirty.

First, I installed puppeti, probably the only thing needed along with git which could be installed by puppet but I want to have a repository for this puppet, so I can keep it updated.

Disclaimer: Probably there are ways to do it better but for me it was easy to 


