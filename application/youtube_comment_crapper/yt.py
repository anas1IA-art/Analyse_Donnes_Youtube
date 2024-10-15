from googleapiclient.discovery import build
import numpy as np
import pandas as pd 


class YtCommentScrapper:
    
    cols = ["videoId", "authorChannelId", "authorDisplayName", "textDisplay",
          "textOriginal", "publishedAt", "updatedAt","likeCount", "canReply" ,"totalReplyCount"]
    
    maxResults = 10000
    videoId = ''
    
    def __init__(self):
        
        self.apiKey = ""
    
    def connect(self):
        self.youtube = build("youtube", "v3", developerKey=self.apiKey)
        
    def comment(self, item):
        item1 = item["snippet"]
    
        snippet = item1["topLevelComment"]["snippet"]
        
        for col in self.cols:
            if col in ("canReply","totalReplyCount"):
                self.data_dict[col].append(item1[col])
            else: 
                s = snippet[col]
                if s != None and s != 'none':
                    if col == "authorChannelId":
                        self.data_dict[col].append(s["value"])
                    else:
                        self.data_dict[col].append(s)
                else:
                    self.data_dict[col].append(np.nan)
        return self.data_dict
    
    def clearDict(self):
        self.data_dict = {col : [] for col in self.cols}
        
    def makeRequest(self):
        self.clearDict()
        request = self.youtube.commentThreads().list(
            part="snippet",
            videoId= self.videoId,
            textFormat="plainText",
            maxResults= self.maxResults,
            order='time'
        )

        response = request.execute()
        while response:
            for item in response["items"]:
                self.data_dict = self.comment(item)
            if 'nextPageToken' in response:
                request = self.youtube.commentThreads().list(
                    part="snippet",
                    videoId= self.videoId,
                    textFormat="plainText",
                    maxResults= self.maxResults,
                    order='time',
                    pageToken=response['nextPageToken']
                )
                response = request.execute()
            else:
                break
    def saveAsCsv(self,name : str):
        if not name.endswith('.csv'):
            name += '.csv' 
        data = pd.DataFrame(self.data_dict)
        data.to_csv(name)

    
    
    
    