# Materiale del corso di ACP

### Installazione dei prerequisiti

```
sudo apt install -y build-essential git gdb manpages-posix manpages-dev manpages-posix-dev vim pkg-config cmake libdbus-glib-1-dev
```

#### Python

Installare l'interprete Python seguendo le guide ufficiali per il proprio SO. Per un sistema Debian-based basta installare:
```
sudo apt update
sudo apt install python3 python3-dev python-is-python3 python3-pip
```

Successivamente installare tutti i package pre-requisiti utilizzando il file [ACP_requirements.txt](ACP_requirements.txt)

```ACP_requirements.txt
$ pip install -r ACP_requirements.txt
```

N.B.: in alcune distribuzioni recenti di Linux, pip non può essere utilizzato se non all'interno di un venv. Per avviare lo stesso l'installazione utilizzare il seguente comando:

```
$ pip install -r ACP_requirements.txt -U --user --force-reinstall --break-system-packages
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

Usare il comando ``codium --install-extension``per installare le estensioni a linea di comando.
  
#### Installazione MongoDB

##### Linux

Avviare lo script di utilità [install_mongodb.sh](install_mongodb.sh):

```
# ./install_mongodb.sh
```

N.B.: lo script di utilità è valido solo per una distribuzione Debian 12. Per l'installazione di MongoDB su altre distribuzione consultare il sito ufficiale [https://www.mongodb.com/docs/manual/tutorial/](https://www.mongodb.com/docs/manual/tutorial/)

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