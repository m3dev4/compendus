# Évaluation des modèles candidats

Ce projet utilise un modèle de résumé de texte. Deux options ont été étudiées avant de choisir le modèle final.

## Modèle 1 : csebuetnlp/mT5_multilingual_XLSum
- Nom sur le Hub : csebuetnlp/mT5_multilingual_XLSum
- Lien : https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum
- Taille : variable selon la configuration et l’environnement, généralement plus lourde qu’un petit modèle de démonstration
- Licence : consultez la page du modèle sur Hugging Face pour vérifier la licence exacte
- Pourquoi ce modèle a été retenu :
  - adapté au résumé de texte dans plusieurs langues
  - intéressant pour un projet plus généraliste et multilingue
  - correspond à l’orientation actuelle du projet

## Modèle 2 : facebook/bart-large-cnn
- Nom sur le Hub : facebook/bart-large-cnn
- Lien : https://huggingface.co/facebook/bart-large-cnn
- Taille : environ 1,6 Go
- Licence : Apache 2.0
- Pourquoi il a été écarté :
  - plus centré sur l’anglais et moins adapté à un usage multilingue
  - moins conforme à l’objectif actuel du projet
  - le modèle mT5 répond mieux à la logique de résumé multi-langue

## Choix final
Le modèle retenu est csebuetnlp/mT5_multilingual_XLSum.

Il a été choisi parce qu’il correspond mieux à l’objectif du projet : proposer un résumé de texte de manière plus polyvalente, y compris pour plusieurs langues.
