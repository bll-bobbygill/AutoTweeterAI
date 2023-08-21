
TWEET_CSV_QA_TEMPLATE="Please return Tweets that relate to any of the following topics: "

GENERATE_TWEETS_TEMPLATE="""
Please generate {number_of_tweets_to_generate} tweets that relate to the topics delimited by <> and are similar in tone to the examples provided below. Tweets must be funny. Tweets must not be serious in tone. Tweets must NOT use hashtags. Tweets must not end in Emoji characters. Format your answer as a list of Tweets, with each individual Tweet on its own line. Each line must end with a newline character.

% START OF EXAMPLE TWEETS TO MIMIC
{example_tweets}
% END OF EXAMPLE TWEETS TO MIMC

<{topics}>

"""

MODERATE_TWEETS_TEMPLATE="""
Delimited in <> are a set of proposed Tweets, please filter out any tweets which have duplicate structure or any Tweets which are offensive or inappropriate. Format your answer as a list of Tweets, with each individual Tweet on its own line. Each line must end with a newline character.
<{final_tweets}>

"""

MAKE_IT_FUNNY_TEMPLATE="""
Listed below are a set of Tweets. Pick and return the 3 wittiest Tweets from that group. Format your answer as a list of Tweets, with each individual Tweet on its own line. Each line must end with a newline character.

{proposed_tweets}
"""