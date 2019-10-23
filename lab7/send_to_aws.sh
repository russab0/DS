#scp -i my_key.pem nginx.conf ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:~/.
#scp -i my_key.pem main.py ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:~/.
#scp -i my_key.pem requirements.txt ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:~/.
#scp -i my_key.pem templates/index.html ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:~/templates
#scp -i my_key.pem templates/contacts.html ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:~/templates

sudo scp -i my_key.pem screen1.png ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:/home/ubuntu
sudo scp -i my_key.pem screen2.png ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:/home/ubuntu
sudo scp -i my_key.pem screen3.png ubuntu@ec2-18-219-163-155.us-east-2.compute.amazonaws.com:/home/ubuntu