import sys
from datetime import timedelta
from youtube_transcript_api import YouTubeTranscriptApi as yt


#Parse YouTube link for video ID
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


def getCC(vid_id):
    try:
        captions = yt.get_transcript(vid_id, languages=['en'])
        for dictionary in captions:
            dictionary['text'] = dictionary['text'].lower()

        return captions
    except:
        return [{'text': 'None'}]
        # quit()


def find(search_term, vid_id, captions):
    """
        Precondition: Use getVideoID(link) to obtain the video ID from the
        YouTube Link, then use getCC(vid_id) to obtain the transcripts.

        Returns a list of lists, one for each line in the transcript that
        contains the search term. Each list has 3 elements:
                0. matching line of transcript text
                1. timestamp of matching line
                2. link to timestamp
    """
    #terms = search_term.split()
    notFound = True
    results = []
    for index, dictionary in enumerate(captions):
        if dictionary['text'] == 'None':
            results.append("NC")

        elif search_term in dictionary['text']:
            notFound = False

            # 0. appearedin, 1.timestamp, 2.link to timestamp
            seconds = int(dictionary['start'])
            results.append([dictionary['text'],
                            str(timedelta(seconds=seconds)),
                            f"https://youtu.be/{vid_id}?t={seconds}",])
        #
        # elif terms[0] in dictionary['text'] and terms[1] in captions[index + 1]['text']:
        #     notFound = False
        #     seconds = int(dictionary['start'])
        #     results.append([dictionary['text'] + captions[index+1]['text'],
        #                     str(timedelta(seconds=seconds)),
        #                     f"https://youtu.be/{vid_id}?t={seconds}",])


    if notFound:
        results.append('NF')


    return results
