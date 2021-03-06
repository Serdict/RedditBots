#Submit a link to submissions from certain subreddits to a target subreddit in certain time intervals.

import praw
import time

user_agent = ('')

timeout = 86400 #seconds
                #In how many seconds the database will be cleared 

visiting_subreddits = ['programming'] #subreddits to crawl
r = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

def main():
        while True:
                time_start = time.time()
                database = [] #store unique links, if the number of submissions is expected to be relatively small, a simple list will suffice
        
                while time.time() < time_start + timeout:
                        post = ""

                        for subreddit in visiting_subreddits:

                                subreddit = r.subreddit(subreddit)                        

                                for submission in subreddit.new(limit=10):
                                        if submission.id not in database:
                                                post += '['+submission.title + ']'+'(' + submission.url + ')' + '\n\n'
                                                database.append(submission.id)
                        if post!="":
                                try:
                                        r.subreddit('bottesting').submit(title='Test Post',selftext=post)
                                except:
                                        time.sleep(600)

if __name__ == '__main__':
        main()
        
