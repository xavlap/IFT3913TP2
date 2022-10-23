# IFT3913 -- TP2
Louis-André Brassard : 20182271
Xavier Lapalme : 20187052

# Lien vers le repo Git 
https://github.com/xavlap/IFT3913TP2

# Commande utilisée pour lancé ckjm sur le repo de jFreeChart, ensuite quelques petits script python3 ont été utilisé 
# pour parse les données générées soit filter_ckjm_LCOM et filter_ckjm_RFC 
```bash
java -jar ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar /home/xavlap/Documents/A22/IFT3913/IFT3913TP2/src/jfreechart-master/src/main/java false 0 false /home/xavlap/Documents/A22/IFT3913/IFT3913TP2/ckmj.csv
```

# Pour trouver le nombre de commit par année sur le repo de JFreeChart
https://gist.github.com/smuuf/0d5746c4e734c51fe0de3559d02cb852
# Commande entrée : résulta dans Data/commit_per_year.txt 
git log --pretty='format:%cd' --date=format:'%Y' | uniq -c | awk '{print "Year: "$2", commits: "$1} > commit_per_year.txt'

# Pour utiliser le API de SonarQube
https://stackoverflow.com/questions/31945139/how-can-i-pull-out-useful-metrics-from-sonarqube

# Api Call dans le fichier open_issue_from_SonarQube.py

# Installation de SonarQube pour ensuite lancer l'analyse avec les commandes suivantes
# sonar-scanner
#     -Dsonar.projectKey=project\
#     -Dsonar.sources=.\
#     -Dsonar.host.url=http://localhost:9000\
#     -Dsonar.login=sqp_383fb4d1e0c0901bf1db4e6b16dff602a06290cf\
#     -Dsonar.java.binaries=target\
#     -Dsonar.analysis.mode=preview
#     -Dsonar.issuesReport.html.enable=true

# Résultats dans Data/SonarQube_open_issues.json

