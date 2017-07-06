`sudo ln -s /home/ubuntu/okapi/server/supervisor_conf.conf /etc/supervisor/conf.d/okapi.conf`

Restart supervisor
`sudo supervisord`

`sudo ln -s /home/ubuntu/okapi/server/nginx.conf /etc/nginx/sites-enabled/okapi`

Copy `server/provision.sql.example` to `server/provision.sql`
