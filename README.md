# Planification de la maintenance des unités de production par algorithme génétique

Ce projet utilise un **algorithme génétique** pour planifier la maintenance de 7 unités de production sur 4 intervalles de temps, en maximisant la **réserve minimale** de puissance sur l'ensemble des intervalles.

## Données du problème

| Unité | Capacité (MW) | Codes de maintenance valides |
|-------|---------------|------------------------------|
| 1     | 20            | 1100, 0110, 0011             |
| 2     | 15            | 1100, 0110, 0011             |
| 3     | 35            | 1000, 0100, 0010, 0001       |
| 4     | 40            | 1000, 0100, 0010, 0001       |
| 5     | 15            | 1000, 0100, 0010, 0001       |
| 6     | 15            | 1000, 0100, 0010, 0001       |
| 7     | 10            | 1000, 0100, 0010, 0001       |

- **Capacité totale installée** : 150 MW
- **Demandes par intervalle** : 80, 90, 65, 70 MW
- Un bit à `1` signifie que l'unité est en maintenance pendant l'intervalle correspondant.

## Principe

- **Chromosome** : liste de 7 blocs de 4 bits (un bloc par unité).
- **Fitness** : réserve minimale sur les 4 intervalles (0 si la solution est invalide).
- **Sélection** : roulette biaisée.
- **Croisement** : en un point entre les blocs (taux de 0,8).
- **Mutation** : inversion du bloc (taux de 0,15), avec repli sur un code valide aléatoire.
- **Paramètres par défaut** : population de 50 individus, 100 générations.

## Exécution

```bash
python h.py
```

### Résultat obtenu

```
Microsoft Windows [version 10.0.26200.9711]
(c) Microsoft Corporation. Tous droits réservés.

C:\Users\bachi\Desktop\machine learning>C:\Users\bachi\miniconda3-pbe\envs\tp1\python.exe "c:/Users/bachi/Desktop/machine learning/h.py"
Meilleur planning trouvé (par unité de 1 à 7) : ['0110', '1100', '0001', '0010', '1000', '0001', '1000']
Réserve minimale garantie (Fitness) : 25.0 MW

C:\Users\bachi\Desktop\machine learning>
```

## Interprétation

Le meilleur planning trouvé garantit une **réserve minimale de 25 MW** sur les 4 intervalles.

## Structure du projet

```
.
├── h.py       # Algorithme génétique
└── README.md  # Documentation
```
