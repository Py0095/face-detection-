from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import socket
import requests  # <-- Utilisation d'une Adresse URL Normalisée
import json  # <-- Permet l'expoitation de fichier en format JSON
import googlemaps  # pip install -U googlemaps <-- API Python de Google MAPS
import socket

import socket

print(socket.gethostbyname(socket.gethostname()))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])

# EXPLICATION --DEBUT--
# Ce Programme est utile pour determine la localisation de l'Adresse IP de l'utilisateur
# En revanche , ce programme n'indique pas la localisation exacte de l'utilisateur, dans ce cas elle sera imprécise!!!
# EXPLICATION --FIN--


# ----------
# API https://ipstack.com

print(socket.gethostbyname(socket.gethostname()))


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])


def get_coordinate_ip():

    send_url = 'http://api.ipstack.com/check?access_key=b0e724b68c170a901019d01552425f1a&format=1'
    # <-- Ouverture de L'URL pour l'utilisation de L'API
    r = requests.get(send_url)
    # Chargement des données reçu dans le fichier en format JSON
    j = json.loads(r.text)

    global latitude  # Declaration de la variable Globale 'latitude'
    global longitude  # Declaration de la variable Globale 'longitude'

    # Information Technique --DEBUT--
    # Enregistrement de l'adresse IP de l'utilisateur dans la Variable Global correspondant
    ip = s.getsockname()[0]
    print('The type: ', type(ip))
    print("Voici votre adresse I.P:", ip)
    # Information Technique --FIN--

    # Information Géographique --DEBUT--
    # Enregistrement de la valeur latitude du fichier JSON dans la Variable Global correspondant
    latitude = j['latitude']
    # Enregistrement de la valeur longitude du fichier JSON dans la Variable Global correspondant
    longitude = j['longitude']

    city = j['city']
    region_name = j['region_name']
    ZIP = j['zip']
    country_name = j['country_name']
    continent_name = j['continent_name']

    # print(latitude)  # Affichage de la Variable 'latitude'
    # print(longitude)  # Affichage de la Variable 'longitude'
    # print("L'adresse IP a ete localiser ici:", city)
    # print("Les Coordonees exactes de l'Adresse IP utilise:",continent_name, country_name, region_name, ZIP, city)
    # Information Géographique --FIN--
    localisation = "Les Coordonees exactes de l'Adresse IP utilise:{},{},{},{},{}".format(continent_name, country_name, region_name, ZIP, city)
    # ,format(continent_name,country_name,region_name,ZIP,city)
    return localisation
    # return latitude,longitude,continent_name,country_name,region_name,ZIP,city      #Retourne les variables obtenue dans le cadre d'une utilisation ultérieur de ses valeurs
# ----------

# INFORMATION :
# La localisation de exacte de l'adresse IP peut être obtenue via l'API /api.ipstack.com/ ou alors en donnant les deux valeurs latitude et longitude à une autre
# A.P.I tel que Google MAPS, qui lui peut obtenir des résultats différents ou plus précis que la première API ; A vous de choisir.

# ----------
# API https://console.cloud.google.com/


def localisation():

    gmaps = googlemaps.Client(
        key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw')  # Cle d'acces A.P.I

    reverse_geocode_result = gmaps.reverse_geocode(
        (latitude, longitude))  # Envoie et Recuperation des Donnees

    print("L'Adresse IP Localise a :")
    # print(reverse_geocode_result) Format JSON

    # STRING LOCALISATION DETERMINE de L'Adresse entière
    resultat_Adresse = reverse_geocode_result[0]['formatted_address']
    # STRING LOCALISATION DETERMINE de La Ville uniquement
    resultat_Ville = reverse_geocode_result[0]['address_components'][2]['long_name']

    # Affichage de l'adresse entière determinée
    print("A l'Adresse suivante :", resultat_Adresse)
    # Afficgage de la Ville determinée
    print("Dans la ville de :", resultat_Ville)

    # Retourne les variables obtenue dans le cadre d'une utilisation ultérieur de ses valeurs
    return resultat_Adresse, resultat_Ville
# ----------


if __name__ == "__main__":
    get_coordinate_ip()  # Fonctionnalité permettant d'Obtenir/Determiné les coordonées GPS correspondant à l'Adresse I.P de l'utilisateur
    # localisation()

# function to send email
def send_email_detection(recipient_email, message, subject):
    sender_email = 'pyp0859@gmail.com'
    password = "yrnjoemiwgzrahpf"
    recipient_email = recipient_email

    # Créer un objet MIMEMultipart pour le message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Corps du message
    message = message
    msg.attach(MIMEText(message, 'plain'))

    # Connexion au serveur SMTP de Gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, password)

    # Envoi du message
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Fermer la connexion au serveur
    server.quit()
    return ("E-mail envoyé avec succès.")


# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

def send_emails_detection(recipient_emails, message, subject):
    sender_email = 'pyp0859@gmail.com'
    password = "yrnjoemiwgzrahpf"

    # Créer un objet MIMEMultipart pour le message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)  # Concatène les adresses avec une virgule
    msg['Subject'] = subject

    # Corps du message
    msg.attach(MIMEText(message, 'plain'))

    # Connexion au serveur SMTP de Gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, password)

    # Envoi du message
    server.sendmail(sender_email, recipient_emails, msg.as_string())

    # Fermer la connexion au serveur
    server.quit()
    return ("E-mails envoyés avec succès.")

# # Liste des adresses e-mail destinataires
# recipient_emails = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']

# # Contenu du message et sujet
# message = "Votre message ici."
# subject = "Sujet du message"

# # Appel de la fonction pour envoyer les e-mails
# send_email_detection(recipient_emails, message, subject)
