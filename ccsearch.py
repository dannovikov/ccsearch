import datetime
from youtube_transcript_api import YouTubeTranscriptApi as yt

#Get YT Link
def getLink(link):
    return link

#Parse for video ID
def getVideoID(link):
    if '?t=' in link:
        link = link.split('?')[-2]
    if '&' in link:
        link = link.split('&')[0] 
    if 'watch?v=' in link:
        link = link.split('watch?v=')[-1]
    if 'youtu.be' in link:
        link = link[-11:]
    return link

#link= getLink(link)
#vid_id = getVideoID(link)

# Get transcript

def getCC(vid_id):
    try:
        captions = yt.get_transcript(vid_id, languages=['en'])
        for dictionary in captions:
            dictionary['text'] = dictionary['text'].lower()
        
        return captions
    except:
        return [{'text': 'None'}]
        # quit()

        
# Get Search Term
#search_term = input('Please enter your search term: ').lower()

def find(search_term, vid_id, captions):
    notFound = True
    with open('templates/results.txt', 'w'):
        pass

    with open('templates/results.txt', 'a') as f:
        for dictionary in captions:
            if dictionary['text'] == 'None':
                f.write('Unfortunately, there are no captions associated with this video.')
                notFound = False
            elif search_term in dictionary['text']:
                f.write(f'{search_term} found in: ')
                f.write('<br>')
                f.write(f'Text: {dictionary["text"]}')
                f.write('<br>')
                seconds = int(dictionary['start'])
                f.write(f'Time stamp: {str(datetime.timedelta(seconds=seconds))}')
                f.write('<br>')
                f.write(f'Link to timestamp: https://youtu.be/{vid_id}?t={seconds}')
                f.write('<br><br><br>')
                notFound = False
        if notFound:
            f.write('Search term was not matched to any captions in this video. Try a smaller search term.')

