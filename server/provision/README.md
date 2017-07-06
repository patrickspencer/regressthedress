# Instructions for ansible server setup

Change in the file `site.yml` change `tag_Name_test` to
`tag_Name_whatever` where "whatever" is the name of the server you are
provisioning. You can also change this to an ip address.

Ssh into the server and git clone the wombat repo to `/home/ubuntu`.
change the data base information variables in `vars/base.yml`
Copy `wombat/settings.py.example` to `wombat/settings.py` and change the
database information

run `ansible-playbook default.yml`

