# Coletas os dados de todos os videos de um canal do Youtube utilizando a Youtube_API
## Get data of every video from a Youtube channel using the Youtube_API

<br>

Os dados coletados são:

> Id do Video, Titulo, Data de Upload, Duracao, Views, Likes, Dislikes, Favoritos, quantidade de comentarios

Tambem há um campo calculado: Total de Views/dias desde lancamento do video, é uma métrica para reconhecer Videos que obtiveram maior audiencia no menor tempo ( média de views desde lançamento do video )


## **Passos de instalação/uso**

1. Clonar repositório e entrar neste diretório 7/
2. Adicionar os IDs dos canais do Youtube no settings.ini
3. Adicionar sua Google API key no setting.ini
4. Instalar as dependencias
5. Executar

```
git clone https://github.com/rodolfo0259/NappAcademy2-2021.git
cd MeuETL/
pip install -r requirements.txt 
```

No settings.ini o campo CHANNEL_ID, pode conter mais de um id de canal, separado por ","