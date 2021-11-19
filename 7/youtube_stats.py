"""
Coleta os detalhes de todos os videos de um determinado canal no youtube
e transforma os dados em um CSV
Dados coletados: 
Id_video, Titulo, DataUpload, duracao, views, likes, dislikes, favoritos, qtd_comentarios
"""
import asyncio
import aiohttp
import requests
import time
import pandas as pd
from datetime import datetime
from datetime import timedelta
import re

from API_KEY import KEY

## API DOC
## https://developers.google.com/youtube/v3/docs/videos/list


CHANNEL_ID = 'UCK3IOOEUXQT-dAl3jy-xkaw' ## BAKA GAIJIN # 24 vids
# CHANNEL_ID = 'UC5e2_0A3A0AvMaZUecvXqZQ'  ## gardarkeres # 5 vids


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
            url = f'https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist_id}&pageToken={nextPageToken}&key={KEY}&part=contentDetails&maxResults=50'
        else:
            break
    return video_ids


async def main(video_ids: list)->None:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for video_id in video_ids:
            task = asyncio.ensure_future(get_video_data(session, video_id))
            tasks.append(task)

        video_statistics = await asyncio.gather(*tasks)

    headers=['Video_id', 'Title', 'Publish_date', 'Duration', 'Views', 'Likes', 'Dislikes', 'FavoriteCount', 'CommentCount']
    df = pd.DataFrame(video_statistics, columns=headers)
    df.to_csv(f'channel_{channel_title}_statistics.csv', sep=';', index=False)
    print('>> CSV gerado <<')


async def get_video_data(session, video_id: str)->list:
    '''
    Coleta os dados de cada video_id
    '''
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={KEY}&part=statistics,contentDetails,snippet'

    async with session.get(url) as response:
        lis = list()
        result_data = await response.json()
        results = result_data['items']
        global channel_title
        channel_title = results[0]['snippet']['channelTitle']

        ## UTF date to UTF-3 (local)
        video_date = results[0]['snippet']['publishedAt']
        video_date = datetime.strptime(video_date, '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=3)
        video_date = video_date.strftime('%Y-%m-%d %H:%M:%S')
        lis.append(results[0]['id'])
        lis.append(results[0]['snippet']['title'])
        lis.append(video_date)

        ## format time duration to iso 8601
        duration = (results[0]['contentDetails']['duration'])
        final_duration = ''
        for i in ['H', 'M', 'S']:
            if duration.find(i) != -1:
                final_duration += ((re.findall(f'(\d+){i}', duration))[0]).zfill(2) + ':'
            else:
                final_duration += '00:'

        lis.append(final_duration[:-1]) ## video_duracao

        ### views, like, dislike, favorite, comments
        data = results[0]['statistics']
        for k, v in data.items():
            lis.append(v)

        return lis


video_ids = get_video_ids(CHANNEL_ID)
asyncio.run(main(video_ids))



