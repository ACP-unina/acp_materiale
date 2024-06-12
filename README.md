# Materiale del corso di ACP

### Installazione dei prerequisiti

#### Python

Installare l'interprete Python seguendo le guide ufficiali per il proprio SO. 
Successivamente installare tutti i package pre-requisiti utilizzando il file [ACP_requirements.txt](ACP_requirements.txt)

```
$ pip install -r ACP_requirements.txt
```

#### Java

Installare Java JDK v1.8 per compatibilità con JMS.
Scegliere la versione in base al proprio SO ([https://www.java.com/it/download/manual.jsp](https://www.java.com/it/download/manual.jsp))

#### VSCodium 

VSCodium ([https://vscodium.com/](https://vscodium.com/)) è l'IDE utilizzato durante il corso. Installare VSCodium in base al proprio SO e le relative estensioni per lo sviluppo di tutti gli esercizi.

- **Python**
  -   ms-python.python
  -   ms-toolsai.jupyter
  -   ms-toolsai.vscode-jupyter-cell-tags
  -   ms-toolsai.jupyter-keymap
  -   ms-toolsai.vscode-jupyter-slideshow
  -   ms-toolsai.jupyter-renderers

- **Java**
  -   vscjava.vscode-java-debug
  -   vscjava.vscode-java-pack
  -   redhat.java
  -   vscjava.vscode-maven
  -   vscjava.vscode-java-dependency

- **MongoDB**
  -   mongodb.mongodb-vscode

- **Protobuf**
  -   zxh404.vscode-proto3  

  
#### Installazione MongoDB

##### Linux

Avviare lo script di utilità [install_mongodb.sh](install_mongodb.sh):

```
# ./install_mongodb.sh
```

##### Mac OSX

```
# brew tap mongodb/brew
# brew update
# brew install mongodb-community@6.0
# brew services start mongodb-community@6.0
```


#### Installazione ActiveMQ 

Installare la ActiveMQ 5.16.6 disponibile a questo [link](https://activemq.apache.org/components/classic/download/classic-05-16-06). 
Scegliere la versione in base al propio SO.