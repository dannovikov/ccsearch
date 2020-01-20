import sys
from datetime import timedelta
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

#rewrite find method to create a list
def find(search_term, vid_id, captions):
    notFound = True
    results = []
    for dictionary in captions:
        if dictionary['text'] == 'None':
            results.append("NC")

        elif search_term in dictionary['text']:
            notFound = False

            # 0. appearedin, 1.timestamp, 2.link to timestamp
            seconds = int(dictionary['start'])
            results.append([dictionary['text'],
                            str(timedelta(seconds=seconds)),
                            f"https://youtu.be/{vid_id}?t={seconds}",])
        elif notFound:
            notFound = True

    if notFound:
        results.append('NF')

    return results
