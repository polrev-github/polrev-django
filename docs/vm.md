## Digital Ocean
Create the VM

Ubuntu 24.04
Intel Premium 2GB/70GB

Host names should be role-environment-region-sequence

Examples:
- web-dev-nyc3-01
- web-staging-nyc3-01
- web-prod-nyc3-01


## Setup

Login as root@ip-address

```bash
apt update
apt upgrade
shutdown -r now
```

## Create Admin User
```bash
adduser kurt
usermod -aG sudo kurt
```
### Switch to the new user's home directory:

```bash
su - kurt
```

### Display your existing public SSH key
Note:  Run this on your machine in a separate terminal
```bash
cat ~/.ssh/id_rsa.pub
```

### Create an .ssh directory and set permissions:
```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

### Copy your SSH public key into the authorized_keys file:
```bash
nano ~/.ssh/authorized_keys
```

### Set the correct permissions:
```bash
chmod 600 ~/.ssh/authorized_keys
```

## Docker Compose

https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

```bash
adduser polrev
usermod -aG docker polrev
su - polrev
docker compose up -d
```

## Create the Docker Compose User
```bash
sudo adduser polrev
sudo usermod -aG docker polrev
```

## Switch to the Docker Compose User
```bash
sudo su - polrev
```

- To be able to ssh into the polrev user repeat the same actions that were used for the admin user

## Clone the Repository
```bash
git clone https://github.com/polrev-github/polrev-django polrev
```

## Copy and Edit the .env File
```bash
cp .env.prod.example .env
nano .env
```

## Copy the docker-compose.prod.yml to docker-compose.override.yml
```bash
cp docker-compose.prod.yml docker-compose.override.yml
```

## Go!
```bash
docker compose up -d
```