"""
Coleta os detalhes de todos os videos de um determinado canal no youtube
e transforma os dados em um CSV
Dados coletados: 
Id_video, Titulo, DataUpload, duracao, views, likes, dislikes, favoritos, qtd_comentarios

## API DOC
## https://developers.google.com/youtube/v3/docs/videos/list
"""
import asyncio
import time
from datetime import datetime
from datetime import timedelta
import requests
import pandas as pd
import aiohttp
import re

from decouple import config, Csv

KEY = config('KEY')
CHANNEL_IDS = config('CHANNEL_ID', cast=Csv())


def get_video_ids(channel_id: str)->list:
    ''' 
    Coleta todos os videos_ids do canal fornecido
    Args: 
        channel_id: codigo do canal no youtube
    Return:
        video_ids: lista com todos os videos id do canal
    '''
    url = f'https://www.googleapis.com/youtube/v3/channels?id={CHANNEL_ID}&key={KEY}&part=contentDetails'

    r = requests.get(url)
    results = r.json()['items']

    ## playlist == channel uploads
    playlist_id = results[0]['contentDetails']['relatedPlaylists']['uploads']

    url = f'https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist_id}&key={KEY}&part=contentDetails&maxResults=50'

    video_ids = []
    while True:
        r = requests.get(url)
        results = r.json()
        nextPageToken = None
        if 'nextPageToken' in results:
            nextPageToken = results['nextPageToken']

        if 'items' in results:
            for item in results['items']:
                videoId = item['contentDetails']['videoId']
                video_ids.append(videoId)

        if nextPageToken:
            url = f'{url}&pageToken={nextPageToken}'
        else:
            break
    return video_ids


async def main(video_ids: list)->None:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for video_id in video_ids:
            task = asyncio.ensure_future(get_video_data(session, video_id))
            tasks.append(task)

        videos_data = await asyncio.gather(*tasks)
        video_data_list = list()
        for video_data in videos_data:
            video_data_list.append(parse_video_data(video_data))
        
        generate_csv(video_data_list)


async def get_video_data(session, video_id: str)->dict:
    '''
    Coleta os dados de cada video_id
    Args:
        session: async session
    Return:
        video_data: dados coletados do video_id fornecido em json
    '''
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={KEY}&part=statistics,contentDetails,snippet'

    async with session.get(url) as response:
        result_data = await response.json()
        video_data = result_data['items'][0]
        return video_data


def parse_video_data(video_data:dict)->list:
    '''
    Tratamento dos dados coletados em json do video
    Args:
        video_data: json/dict com os dados do video
    Return:
        parsed_list: lista com os dados tratados
    '''
    parsed_list = list()
    global channel_title
    channel_title = video_data['snippet']['channelTitle']
    parsed_list.append(video_data['id'])
    parsed_list.append(video_data['snippet']['title'])

    ## UTF date to UTF-3 (local)
    video_date = video_data['snippet']['publishedAt']
    video_date = datetime.strptime(video_date, '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=3)
    parsed_list.append(video_date.strftime('%Y-%m-%d %H:%M:%S'))

    ## format e.g. PT1H23M03S time duration to iso 8601
    duration = (video_data['contentDetails']['duration'])
    final_duration = ''
    for i in ['H', 'M', 'S']:
        if duration.find(i) != -1:
            final_duration += ((re.findall(f'(\d+){i}', duration))[0]).zfill(2) + ':'
        else:
            final_duration += '00:'

    parsed_list.append(final_duration[:-1]) ## video_duration

    ## statistica sobre os videos
    ## videos com comentarios bloqueado vira None
    itens = ['viewCount', 'likeCount', 'dislikeCount', 'favoriteCount', 'commentCount']
    data = video_data['statistics']
    for field in itens:
        parsed_list.append(data.get(field,'None'))

    ## Views/days since video release
    view_day = int(data['viewCount'])/(int((datetime.today() - video_date ).days)+1)
    parsed_list.append(round(view_day, 3))

    return parsed_list


def generate_csv(video_data_list:list)->None:
    '''
    Gera um csv usando o nome do canal com os dados coletados
    '''
    headers=['Video_id', 'Title', 'Publish_date', 'Duration', 'Views', 'Likes', 'Dislikes', 'FavoriteCount', 'CommentCount', 'View/day']
    df = pd.DataFrame(video_data_list, columns=headers)
    df.to_csv(f'channel_{channel_title}_statistics.csv', sep=';', index=False)
    print(f'>> CSV gerado do canal {channel_title} <<')


for CHANNEL_ID in CHANNEL_IDS:
    video_ids = get_video_ids(CHANNEL_ID)
    asyncio.run(main(video_ids))
