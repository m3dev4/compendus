# Évaluation des modèles candidats

Ce projet utilise un modèle de résumé de texte. Deux options ont été étudiées avant de choisir le modèle final.

## Modèle 1 : facebook/bart-large-cnn
- Nom sur le Hub : facebook/bart-large-cnn
- Lien : https://huggingface.co/facebook/bart-large-cnn
- Taille : environ 1,6 Go
- Licence : Apache 2.0
- Pourquoi ce modèle a été retenu :
  - très connu et largement utilisé pour les tâches de résumé de texte
  - bon compromis entre qualité de résumé et simplicité d’utilisation
  - adapté à un projet de démonstration et de test local

## Modèle 2 : google/pegasus-xsum
- Nom sur le Hub : google/pegasus-xsum
- Lien : https://huggingface.co/google/pegasus-xsum
- Taille : environ 2,4 Go
- Licence : Apache 2.0
- Pourquoi il a été écarté :
  - plus lourd à charger
  - moins pratique pour un démarrage rapide sur un environnement local
  - la qualité est intéressante, mais le modèle BART est plus simple à intégrer ici

## Choix final
Le modèle retenu est facebook/bart-large-cnn.

Il a été choisi parce qu’il est plus simple à utiliser, plus accessible pour les débutants et suffisant pour la fonctionnalité principale du projet : résumer un texte de manière claire et rapide.
