# README file disponibile durante gli esami

## Tips and Tricks

### Python STOMP

* La ``Connection`` deve essere stabilita su host ``127.0.0.1`` e porto ``61613``

* Nel caso di traccia in cui il sistema da sviluppare include entità JMS e entità STOMP, utilizzare 
``auto_content_length=False`` per creare la ``Connection``

* Nel caso di traccia in cui il sistema da sviluppare include entità JMS e entità STOMP, e si intende popolare l'header JMSReplyTo, in fase di send lato STOMP popolare l'header STOMP reply-to con il nome della destination (coda o topic): ``headers={"reply-to":"/queue/nome_queue"}`` (questo esempio è relativo ad una coda)

### Java JMS

Utilizzare le seguenti proprietà per JNDI:


* ``"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"``
* ``"java.naming.provider.url" -> "tcp://127.0.0.1:61616"``

N.B.: Quando si lancia un software JMS è necessario includere il file ``.jar`` di ActiveMQ nel classpath. Ad esempio: 

``java -cp "/path_al_file_jar:" nome_package.nome_classe``

Fare attenzione al separatore ``:`` al termine del path specificato.

### Dashboard ActiveMQ

* **Url:** ``http://localhost:8161``
* **Username:** admin
* **Password:** admin

N.B.: La dashboard è disponibile solo dopo aver avviato ActiveMQ

### GRPC - Python

* Per la compilazione, posizionarsi nella cartella che contiene il file .proto ed utilizzare il seguente comando: ``python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./nome_file.proto``

* Per creare un server, generando un'eccezione se il porto è già utilizzato, immettere la segente opzione nella creazione del server GRPC: ``options=(('grpc.so_reuseport', 0),)``

### GRPC - Java

* Per la compilazione, posizionarsi nella cartella che contiene il file .proto ed utilizzare il seguente comando: ``protoc --java_out=. --grpc-java_out=. --plugin=protoc-gen-grpc-java=/PATH/TO/protoc-gen-grpc-java-plugin nome_file.proto``

### Flask

* Il porto di default utilizzato da un applicativo Flask è ``5000``

### MongoDB

* Il servizio mongodb può essere avviato con il comando: ``sudo systemctl start mongod``
* La connection string di default è: ``mongodb://127.0.0.1:27017``
* E' possibile verificare la connection string attraverso la command line ``mongosh`` 


### Creazione ZIP file per upload su github classroom
* Aprire un terminale
* Posizionarsi (utilizzando il comando ``cd``) nel path che contiene la cartella con il codice sviluppato
* Digitare il seguente comando
``zip -r NOME_COGNOME_MATRICOLA_DOCENTE.zip NOME_CARTELLA_CODICE``


