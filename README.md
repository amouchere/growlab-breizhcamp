# `#growlab` app for Raspberry Pi

Enregistrement de données issues d'un potager connecté. 

![](https://pbs.twimg.com/media/E0DwywWXoAET9dK?format=jpg&name=medium)
> The [@alexellisuk](https://twitter.com/alexellisuk) growlab preview

Inspiré par le [projet d'Alex Ellis](https://github.com/alexellis/growlab)


### Fonctionnalités

* prise de photo à interval régulier
* stockage des photos pour création d'un timelapse
* utilisation d'un sensor DHT22 (température et humidité) pour incruster dans les photos
* publier la dernière photo sur une page statique servie par un Nginx

### Configurer le RPi

en utilisant la commande `raspi-config`

* Enable i2c under interfacing options
* Change the password for the `pi` user

### Installation du software

Installation de git :

```bash
sudo apt update -qy
sudo apt install -qy git
```


Installation du projet :

```bash
# clone project
git clone git@github.com:amouchere/growlab-breizhcamp.git

cd ~/growlab-breizcamp
./install.sh
```
### Utilisation

Un Grafana exposant les métriques est accessible sur http://localhost:3000

La page Live du growlab est accessible sur http://localhost:80


### Hardware 

* Bois de récupération
* Raspberry pi V3 avec Wifi
* Caméra compatible RPI
* Capteur DHT22, BMP280
* On/Off Boutton pour éteindre le RPI sans session ssh
* On/Off Boutton pour déclencher un arrosage grâce au projet growlab-watering


TODO : Ajout photos