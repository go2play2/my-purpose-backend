from util import db_util


class TweetDao:
    def __init__(self) -> None:
        pass


    def insert_tweet(self, user_id, tweet):
        con, cursor = db_util.get_connection()

        cursor.execute("""
            INSERT INTO mt_tweets (
                user_id,
                tweet
            ) VALUES ( %s, %s )
            """,
            (user_id, tweet)
        )

        result = cursor.rowcount

        con.commit()
        db_util.close(con, cursor)

        print("*** new tweet inserted")
        return result



    def select_timeline(self, user_id):
        con, cursor = db_util.get_connection()

        exe_result = cursor.execute("""
            SELECT 
                t.user_id,
                t.tweet
            FROM mt_tweets t
            LEFT JOIN mt_users_follow_list ufl ON ufl.user_id = %s
            WHERE t.user_id = %s
            OR t.user_id = ufl.follow_user_id
            """, (
                user_id, user_id
            )
        )
        
        print("=== execute result: ", exe_result)
        tweets = cursor.fetchall()

        print("=== tweets from DB: ", tweets)

        db_util.close(con, cursor)

        return tweets
