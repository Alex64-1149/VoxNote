**VoxNote : Site web Django fournissant un accès à une IA de reconnaissance vocale créée à l'aide de PyTorch**

  VoxNote est une application web transformant la voix en texte en utilisant l’intelligence artificielle. À l’aide de celle-ci, on peut envoyer des vox qui sont comme des notes écrites sans qu’on ait besoin de les écrire. Nous gardons toutefois la possibilité de modifier le texte à posteriori si pour pouvoir retravailler le texte et corriger les erreurs. Ce site a pour but de permettre d’envoyer de l’information plus rapidement que des courriels ou des textos puisque l'homme parle généralement plus vite qu'il écrit. Cette application permet donc de formuler des messages vocaux de façon plus rapide que lors d'une saisie manuscrite. 
  
  Ce projet est fait dans un cadre éducatif. Par conséquent, il n’est pas innovateur par son concept, mais plutôt par les connaissances que nous allons acquérir. En effet, ce projet nous a permis d'apprendre les fondements de l’IA ainsi que ceux de l’interface web. Des compétences que nous n’avions pas acquises précédemment. Ce projet possède donc un certain avantage par la quantité de commentaires pour expliquer chaque étape de sa conception, ce qui peut aider à la compréhension pour ceux n'ayant pas ou peu touché à ces deux domaines de la programmation.

**Informations sur l'IA** <br/>
Il est à noter l'aide non négligeable du blog de Ketan Doshi (https://ketanhdoshi.github.io/Audio-ASR/) dans toutes les étapes de la confection de l'IA pour l'excellente description du traitement audio requis ainsi que pour les informations générales nécessaires à la création d'une IA de reconnaissance vocale comme le type de modèle et le type de loss function à préconiser (CTC loss function). De même, une publication d'AssemblyAI (https://www.assemblyai.com/blog/end-to-end-speech-recognition-pytorch/) a été très utile pour préciser les différentes composantes nécessaires à l'IA en fournissant du code avec lequel comparer – même si le type de modèle n'est pas exactement le même et a été écrit par des personnes nettement plus expérimentées –. Finalement, la documentation PyTorch (https://pytorch.org/docs/stable/index.html) de toutes ses méthodes a été très utile pour la compréhension de leur utilisation ainsi que pour déboguer le code.<br/>
*Dataset*<br/>
Le dataset utilisé – The SIWIS French Speech Synthesis Database – peut être retrouvé à l'addresse suivante : https://datashare.ed.ac.uk/handle/10283/2353. Il a été créé par des chercheurs de l'Université d'Édimbourg et contient ~10h de phrases en français séparées en cinq catégories distinctes. Il a l'avantage d'être un des seuls dataset en français qui est gratuit et possède des fichiers détaillés faciles d'utilisation.<br/>
*Traitement des fichiers audio*<br/>
Le traitement des fichiers audios s'est fait à l'aide de TorchAudio en utilisant un excellent tutoriel dont on peut retrouver le github à l'addresse suivante : https://github.com/musikalkemist/pytorchforaudio.<br/>
*Type d'IA*<br/>
Le type choisi, un modèle LSTM – long short-term memory –, est une sous catégorie des « Recurrent Neural Network » et est très utile pour les IA ayant besoins d'analyser de l'information séquentielle. Ce type est très bien vulgarisé sur le blog suivant : https://colah.github.io/posts/2015-08-Understanding-LSTMs/. <br/>

*Résultats*<br/>
|époque 1|90,13%|<br/>
|époque 3|88,22%|<br/>
|époque 5|86,95%|<br/>
|époque 7|85,94%|<br/>
|époque 9|86,01%|<br/>
Après 10 époques, l'IA stagne vers 85% d'erreurs.

*Améliorations potentielles*<br/>
Il est à noter que le dataset comprend des valeurs qui sont toutes de même taille alors que les phrases enregistrées ne le sont pas. De même le nombre de valeurs inférées maximum est à 128 ; rendre variables ces valeurs – surtout celles du dataset – pourraient grandement améliorer les performances. De plus, l'approche la plus souvent utilisée est celle d'un LSTM associé à un CNN de quelques profondeurs ; ce qui n'a pas été fait dans ce projet nous introduisant à l'IA même si les performances en sont améliorées. Finalement, nous avons utilisé le GreedySearch lors de l'inférence même si le BeamSearch peut fournir de bien meilleurs résultats par manque de temps ainsi que par manque de «language model» en français.

**Informations sur le site web**

L'application web a été entièrement créée à l'aide de Django. Le site web offre la possibilité à ses visiteurs de tester l'IA que nous avons réalisée en enregistrant un message vocal qui sera ensuite transmis à notre modèle entrainé qui retournera une réponse sous la forme de texte. Tout les messages renvoyés par l'IA sont enregistrés dans la base de données. Un utilisateur qui souhaite encore plus profiter des différents avantages du site a la possibilité de se créer un compte en se choisisant un nom d'utilisateur et un mot de passe. Une fois le compte créé, l'utilisateur peut se connecter à l'aide de son identifiant et de son mot de passe et il accède à la fonctionnalité principale de notre application web. Lorsque connecté, l'utilisateur peut toujours envoyer des messages vocaux à l'IA, mais maintenant, chaque réponse de notre IA est enregistrée sous la forme de note ou de tâche à réaliser. L'utilisateur connecté peut accéder à toutes les notes qu'il a déjà enregistré dans la base de données en cliquant sur l'onglet mes notes. Cet onglet est organisé pour que les notes soient affichées horizontalement une à la suite de l'autre de la plus récente à la plus vieille. Les notes prennent la formes de petites boites avec au sommet la date et au milieu le contenu reconnu par notre IA. Si l'utilisateur veut voir le contenu d'une note de manière plus détaillée, il peut le faire en cliquant sur le bouton voir la note qui est placé en bas d'une note. Lorsque l'utilisateur clique sur le bouton, il voit maintenant la note qu'il a choisie en plein milieu de son écran et en grand plan. Après avoir observé sa note qu'il a choisi, l'utilisateur peut décider de revenir à sa liste de notes ou de supprimer une note parce qu'il n'en a plus besoin où s'il a fini la tâche qu'il devait faire. Si l'utilisateur appuie sur le bouton supprimer, une page qui demande à l'utilisateur de confirmer son choix apparait et deux options sont proposés à l'utilisateur. La première est de revenir à la note et la deuxième est de confirmer la supprimation de la note. Si l'utilisateur appuie sur le bouton confirmer, la note choisie est effacée de la base de donnée et n'est plus affichée sur l'onglet mes notes. Un utlisateur connecté a la possibilité de se connecter en tout temps. N'importe quel utilisateur connecté peut accéder à la page à propos du site où des information sur comment notre IA a été construite sont affichés.<br/>

La série de tutoriels de Dom Vacchiano https://www.youtube.com/watch?v=w7EJu9Gd5Ns&list=PLQbt1tI_yQHg5HYpdUqit1wkc4BOPTkpx&ab_channel=DomVacchiano a été une très bonne introduction aux application Django en construisant une application full-stack de recettes.<br/>

La page de tutoriel Geeks for Geeks https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/ nous a aidé a programmer le système d'authentification de l'application web.<br/>

Le tutoriel de Tyler Potts https://www.youtube.com/watch?v=3OnMBtOyGkY&ab_channel=TylerPotts nous a aidé a transformer l'input du micro en fichier audio.<br/>

*Améliorations potentielles*<br/>
Nous avions également beaucoup d’autres fonctionnalité qu’on aurait aimé ajouter avec plus de temps. Premièrement nous aurions ajouté l’option d’interagir avec d’autres individus utilisant Voxnote en mettant en place un système de texto comme Microsoft équipes, seulement avec les textes transformés par l’IA à partir d’un message vocal de l’utilisateur donc en ne laissant pas l’utilisateur écrire un texte sur le clavier. On aurait ajouté l’option d’ajouter des amis et d’entamer des conversations privées ou en groupe. Ensuite, nous aurions ajouté l’option pour un utilisateur de se connecter avec google pour simplifier la connexion. Nous aurions aussi donné l’option à un utilisateur connecté avec son adresse courriel (Gmail, Yahoo ,Outlook etc.) de pouvoir envoyer un email en un seul clic directement après avoir généré la réponse de l’IA. Finalement, le but ultime aurait été de créer une application mobile à partir de notre application web parce que notre IA deviendrait encore plus accessible aux personnes qui utilisent plus des applications mobiles que des applications web.





**Auteurs**
Jérémie Lestage et Alexandre Tancrède

