# Commands

## terminate instance:
`aws ec2 terminate-instances --instance-ids <instance id>`

## links
[Aws dynamic inventory](https://aws.amazon.com/blogs/apn/getting-started-with-ansible-and-dynamic-amazon-ec2-inventory-management/)

[Ansible aws guide](http://docs.ansible.com/ansible/guide_aws.html)

## ssh:
get public_dns_name from `py aws.py show`

`ssh -i ~/.ssh/patrick-x240-2.pem <public_dns_name>`

`scp -i ~/.ssh/patrick-x240-2.pem initial_setup.sh ubuntu@ec2-54-196-80-181.compute-1.amazonaws.com:/home/ubuntu/ `

`ansible -i /etc/ansible/ec2.py -u ubuntu us-east-1 -m ping`

`ansible -m ping tag_Name_insight -u ubuntu`

