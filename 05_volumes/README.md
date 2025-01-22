# Tutorial: Eseguire Container Docker con Volumi

Questo tutorial ti guiderà nell'esecuzione di un container Docker utilizzando volumi per persistere i dati e condividerli tra il container e il sistema host.


## Cos'è un Volume Docker?

Un volume Docker è una parte del filesystem che viene gestita da Docker. I volumi consentono di persistere i dati in modo che non vengano persi quando il container viene fermato o rimosso. I volumi possono essere utilizzati anche per condividere i dati tra più container o tra un container e l'host.


## Passaggio 1: Creare un Volume Docker

Per creare un volume Docker, puoi utilizzare il comando `docker volume create`. Questo comando crea un volume vuoto che può essere utilizzato dai container.

```bash
docker volume create my-volume
```

**Spiegazione**:  
- `my-volume`: è il nome del volume che stai creando. Puoi scegliere qualsiasi nome.

Per verificare che il volume sia stato creato correttamente, puoi usare:

```bash
docker volume ls
```


## Passaggio 2: Eseguire un Container con un Volume

Ora puoi eseguire un container utilizzando il volume che hai creato. Puoi fare ciò mappando il volume a una directory del container.

```bash
docker run -it -v my-volume:/data --name my-container ubuntu
```

**Spiegazione**:
- `-v my-volume:/data`: Mappa il volume `my-volume` alla directory `/data` all'interno del container.
- `--name my-container`: Assegna al container il nome `my-container`.
- `ubuntu`: è l'immagine del container (in questo caso, stiamo utilizzando l'immagine ufficiale di Ubuntu).

In questo esempio, il volume viene montato nella directory `/data` all'interno del container. Qualsiasi dato scritto in `/data` all'interno del container sarà memorizzato nel volume Docker e persisterà anche dopo che il container verrà fermato o rimosso.


## Passaggio 3: Scrivere e Leggere Dati dal Volume

Una volta dentro il container, puoi scrivere dei dati nella directory `/data` che è montata dal volume:

```bash
echo "Ciao, mondo!" > /data/hello.txt
```

Per verificare che il file sia stato creato, puoi leggere il file all'interno del container:

```bash
cat /data/hello.txt
```

Uscendo dal container, puoi verificare che i dati siano persistere nel volume. Puoi farlo creando un nuovo container che monta lo stesso volume.


## Passaggio 4: Montare il Volume in un Nuovo Container

Esegui un nuovo container che monta lo stesso volume per verificare che i dati siano stati conservati:

```bash
docker run -it --rm -v my-volume:/data ubuntu bash
```

All'interno di questo nuovo container, puoi accedere al file che hai creato in precedenza:

```bash
cat /data/hello.txt
```

Dovresti vedere l'output:

```bash
Ciao, mondo!
```

Questo dimostra che i dati nel volume sono persistere e sono accessibili da più container.


## Passaggio 5: Rimuovere il Volume

Quando non hai più bisogno del volume, puoi rimuoverlo. Prima, assicurati che nessun container stia usando il volume:

```bash
docker ps -a
```

Poi, rimuovi il volume con il comando:

```bash
docker volume rm my-volume
```

Se il volume è ancora in uso da un container, non sarà possibile rimuoverlo finché non rimuovi il container associato.


## Suggerimenti

- I volumi sono gestiti da Docker e sono più efficienti rispetto ai bind mount, poiché sono ottimizzati per l'uso in container.
- Puoi anche mappare una directory del sistema host a una directory del container, ma i volumi sono preferibili per la persistenza dei dati.
- Puoi usare volumi condivisi tra container per implementare architetture di microservizi che necessitano di una memoria persistente condivisa.
