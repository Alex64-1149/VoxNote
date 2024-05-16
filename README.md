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
Il est a noter que le dataset comprend des valeurs qui sont toutes de même taille alors que les phrases enregistrées ne le sont pas. De même le nombre de valeurs inférées maximum est à 128 ; rendre variables ces valeurs – surtout celles du dataset – pourraient grandement améliorer les performances. De plus, l'approche la plus souvent utilisée est celle d'un LSTM associé à un CNN de quelques profondeurs ; ce qui n'a pas été fait dans ce projet nous introduisant à l'IA même si les performances en sont améliorées. Finalement, nous avons utilisé le GreedySearch lors de l'inférence même si le BeamSearch peut fournir de bien meilleurs résultats par manque de temps ainsi que par manque de «language model» en français.

**Informations sur le site web**


**Auteurs**
Jérémie Lestage et Alexandre Tancrède

