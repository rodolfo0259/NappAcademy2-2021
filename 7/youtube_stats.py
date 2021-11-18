"""
Feito para coletar detalhes de todos os videos de um determinado canal no youtube
e transforma os dados em um csv com o titulo de cada video e seus detalhes
Dados coletados: titulo, duracao, views, likes, dislikes, quantidade de comentarios
"""
import asyncio
import aiohttp
import requests
import time
import pandas as pd

from API_KEY import KEY


# channel_id = 'UC7YOGHUfC1Tb6E4pudI9STA'  ## mental Outlaw # 531 vids
channel_id = 'UC5e2_0A3A0AvMaZUecvXqZQ'  ## gardarkeres # 5 vids


def get_video_ids(channel_id: str)->list:
    ''' 
    Coleta todos os videos_ids do canal fornecido
    Args: 
        channel_id: codigo do canal no youtube
    Return:
        video_ids: lista com todos os videos id do canal
    '''
    url = f'https://www.googleapis.com/youtube/v3/channels?id={channel_id}&key={KEY}&part=contentDetails'
    r = requests.get(url)
    results = r.json()['items']

    ## playlist -> channel uploads
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


async def main(video_ids: list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for video_id in video_ids:
            task = asyncio.ensure_future(get_video_data(session, video_id))
            tasks.append(task)

        video_statistics = await asyncio.gather(*tasks)

    headers=['Video_id', 'Views', 'Likes', 'Dislikes', 'Favorites', 'Comments']
    df = pd.DataFrame(video_statistics, columns=headers)
    df.to_csv(f'channel_{channel_id}_statistics.csv', sep=';', index=False)
    print('CSV gerado')
    # print('Number of videos:', len(video_statistics))
    # print('Average number of views:', sum(video_statistics) / len(video_statistics))


async def get_video_data(session, video_id: str):
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={KEY}&part=statistics'

    ## paramentro part ?! traz dados solicitados 
    ## https://developers.google.com/youtube/v3/docs/videos/list
    async with session.get(url) as response:
        result_data = await response.json()
        results = result_data['items']
        data = results[0]['statistics']

        return [results[0]['id'], data['viewCount'], data['likeCount'], data['dislikeCount'], data['favoriteCount'], data['commentCount']]


video_ids = get_video_ids(channel_id)
asyncio.run(main(video_ids))
