# About

Project Wombat (i.e. Regress The Dress) is a python app for Style Lend
anayltics. Stylelend is an online company that helps women lend their
clothes to others. The current problem is that a user must first send
their items into Stylelend.com in order to find out how much their item
is worth. This application is a price prediction application that
Stylelend users can use to find out how much their items are worth just
by entering in a few details about the item.

# Instructions for ansible server setup

Change in the file `site.yml` change `tag_Name_test` to
`tag_Name_whatever` where "whatever" is the name of the server you are
provisioning. You can also change this to an ip address.

- ssh into the server and git clone the wombat repo to `/home/ubuntu`.
- change the data base information variables in `vars/base.yml`
- copy `wombat/settings.py.example` to `wombat/settings.py` and change the
  database information
- run `ansible-playbook site.yml` in the directory `server/provision/`

# Instructions for installing a development machine

- Change directory into folder with the file setup.py and then run `python
  setup.py develop`.
- Run `pip install -r requirements.txt` in the base folder to install
    all the requirements.
- Then copy `stylelend/settings.py.example` to `stylelend/settings.py` and change the
  variables in the file. 
