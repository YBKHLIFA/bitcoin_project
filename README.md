# Suivi en temps réel du taux de change BTC/USD #

## Contexte du projet

Ce projet a été réalisé dans le cadre d’un travail pratique visant à mettre en œuvre une solution légère de surveillance des données financières en temps réel, sans passer par des APIs externes nécessitant des clés d’accès.  
Le choix s’est porté sur le Bitcoin (BTC) en tant que valeur de référence, et l’outil devait permettre de :
- Collecter le prix du BTC toutes les 5 minutes
- Visualiser l’évolution du taux sur un dashboard web
- Générer un rapport quotidien récapitulatif à 20h

## Objectifs pédagogiques
- Mettre en œuvre un scraping simple avec `curl` et Bash
- Manipuler des données temporelles avec `pandas`
- Construire une interface web dynamique avec `Dash` (Python)
- Automatiser les tâches via `cron`
- Déployer une application en ligne accessible via IP

## Fonctionnalités
- Scraping du taux BTC/USD toutes les 5 minutes depuis CoinGecko
- Stockage dans un fichier CSV (`btc_data.csv`)
- Dashboard web actualisé automatiquement
- Génération d’un rapport texte chaque jour à 20h (`daily_report.txt`)
- Interface graphique avec dernier taux affiché et graphique d’évolution

## Exemple de données générées
2025-05-18 14:25:00,104652
2025-05-18 14:30:00,104760
2025-05-18 14:35:00,104775

## Exemple du rapport (`daily_report.txt`)
Daily BTC/USD Report – Sun May 18 20:00:00 UTC 2025
2025-05-18 14:25:00,104652
2025-05-18 14:30:00,104760
Tâches configurées via `crontab -e` :

## cron
*/5 * * * * /home/ubuntu/bitcoin_project/scraper.sh
0 20 * * * /home/ubuntu/bitcoin_project/report.sh

## Lancer l’environnement virtuel 
python3 -m venv venv
source venv/bin/activate
pip install dash pandas plotly

## Démarrer l'application 
python dashboard.py

## Dashboard accessible sur 
“  http://13.51.200.189:8050/ “

