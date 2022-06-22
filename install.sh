# https://learnraspberrypi.com/2019/08/07/setup-wifi-and-ssh-on-raspberry-pi-without-a-monitor/

curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
groups pi

sudo apt-get update && sudo apt-get -y upgrade
sudo apt install -y git \
    zsh python3-pip 
    python3 \
    python3-pip \
    libopenjp2-7 \
    libopenjp2-7-dev \
    libopenjp2-tools
# The `libopenjp2` package is for overlaying text on top of the images.

git config --global user.email "a.mouchere@protonmail.com"
git config --global user.name "AMouchere"

 
# Installation de OhMyZsh à la fin. Le prompt final pour set le shell par défaut emepche la suite du script. 
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Installation de Docker-compose https://sanderh.dev/setup-Docker-and-Docker-Compose-on-Raspberry-Pi/
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
sudo pip3 -v install docker-compose
docker-compose --version


# general log directory
mkdir -p /home/pi/data/log

# Répertoire de stockage des data grafana et influxdb (volume)
mkdir -p ~/data/influxdb
mkdir -p ~/data/grafana

sudo chmod 777 -R ~/data


# Growlab BreizhCamp
mkdir -p ~/growlab-breizhcamp
mkdir -p ~/growlab-live

cd ~/growlab-breizhcamp
curl -sSL https://github.com/googlefonts/roboto/releases/download/v2.138/roboto-unhinted.zip -o roboto.zip
unzip roboto.zip -d roboto
rm roboto.zip

# growlab preview static resources
cp ~/growlab-breizhcamp/static/*.* ~/growlab-live/

# growlab python dependencies
sudo pip3 install -r ~/growlab-breizhcamp/requirements.



# Installation du service pour le bouton shutdown. 
cd ~
git clone https://github.com/amouchere/raspberry-scripts.git

# Dépendance nécessaire pour l'utilisation des ports GPIO
sudo apt-get install -y python3-gpiozero
sudo cp /home/pi/raspberry-scripts/shutdown-button.service /etc/systemd/system/shutdown-button.service
sudo systemctl enable shutdown-button.service
sudo systemctl start shutdown-button.service

# Installation du service de la solution growlab-watering
cd ~
git clone https://github.com/amouchere/growlab-watering.git

sudo cp ~/growlab-watering/watering.service /etc/systemd/system/watering.service
sudo systemctl enable watering.service
sudo systemctl start watering.service

# Installation des services backend du breizhcamp growlab
sudo cp ~/growlab-breizhcamp/growlab-bzh-backend.service /etc/systemd/system/growlab-bzh-backend.service
sudo systemctl enable growlab-bzh-backend.service
sudo systemctl start growlab-bzh-backend.service

# Installation du programme python growlab breizhcamp
sudo cp ~/growlab-breizhcamp/growlab-bzh-python.service /etc/systemd/system/growlab-bzh-python.service
sudo systemctl enable growlab-bzh-python.service
sudo systemctl start growlab-bzh-python.service