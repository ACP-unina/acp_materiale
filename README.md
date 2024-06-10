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

Installare VSCodium e le relative estensioni per lo sviluppo in Python e Java.

- Code Runner (formulahendry)
- Jupyter (ms-toolsai)
- Jupyter Cell Tags (ms-toolsai)
- Jupyter Keymap (ms-toolsai)
- Jupyter Notebook Renderers (ms-toolsai)
- Jupyter Slide Show (ms-toolsai)
- Python (ms-python)
- Python Debugger (ms-python)

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