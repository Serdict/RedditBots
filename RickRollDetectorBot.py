import praw
from praw.models import MoreComments
import time


r = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')


def main():

        while True:
                
                mult_r_h = r.subreddit('bottesting+requestabot').hot(limit=10) #subreddits to crawl and number of posts per check
                mult_r_n = r.subreddit('bottesting+requestabot').new(limit=10) #get both hot and new submissions from target subs
                for sub in [mult_r_h,mult_r_n]:
                        for  submission in sub:

                                submission.comments.replace_more(limit=0)
                                
                                for comment in submission.comments.list():
                                        while True:
                                                try:
                                                        if sum(("v="+["dQw4w9WgXcQ","oHg5SJYRHA0","6_b7RDuLwcI"][i]) in comment.body for i in range(3))>=1:#Check for Rick Roll YouTube ids in comment
                                                                if sum((cc.author==r.user.me() for cc in comment.replies))==0: #Check whether you have already replied to the comment
                                                                        comment.reply("RICK ROLL DETECTED") #Post body
                                                        break
                                                except:
                                                        time.sleep(10)
                                                        
                
                time.sleep(90) #seconds staying idle
                for comment in r.redditor(r.user.me().name).comments.new(limit=10): #get your last comments
                        if comment.score>=100 and not comment.edited:
                                while True:
                                        try:
                                                comment.edit("RICK ROLL \n THIS IS THE NEW TEXT") #if a recent comment has more than 100 upvotes, edit the comment
                                        except:
                                                time.sleep(10)
                time.sleep(90) #seconds staying idle
                                        

if __name__ == '__main__':
        main()        
