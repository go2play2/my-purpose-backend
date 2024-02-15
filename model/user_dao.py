from util import db_util, str_util


class UserDao:
    def __init__(self) -> None:
        pass


    def insert_user(self, user):
        con, cursor = db_util.get_connection()

        cursor.execute("""
            INSERT INTO mt_users (
                name,
                email,
                profile,
                hashed_password
            ) VALUES (%s, %s, %s, %s)
        """, (
            user['name'], 
            user['email'], 
            user['profile'], 
            user['password'] )
        )

        new_user_id = cursor.lastrowid

        con.commit()
        db_util.close(con, cursor)

        print("*** new user inserted(id): ", new_user_id)
        return new_user_id


    def select_user(self, user_id):
        con, cursor = db_util.get_connection()

        exe_result = cursor.execute("""
            SELECT 
                id,
                name,
                email,
                profile
            FROM mt_users
            WHERE id = %s
            """, (user_id,))
        
        print("=== execute result: ", exe_result)
        user = cursor.fetchone()

        print("=== user from DB: ", user)

        db_util.close(con, cursor)

        return user



    def insert_follow(self, user_follow):
        con, cursor = db_util.get_connection()

        cursor.execute("""
            INSERT INTO mt_users_follow_list (
                user_id,
                follow_user_id
            ) VALUES ( %s, %s )
        """, (
            str_util.get_value(user_follow, 'id'), 
            str_util.get_value(user_follow, 'follow'), 
        ))

        result = cursor.rowcount

        con.commit()
        db_util.close(con, cursor)

        print("*** new follow inserted")
        return result



    def delete_follow(self, user_unfollow):
        con, cursor = db_util.get_connection()

        cursor.execute("""
            DELETE FROM mt_users_follow_list
            WHERE user_id = %s
            AND follow_user_id = %s
        """, (
            str_util.get_value(user_unfollow, 'id'), 
            str_util.get_value(user_unfollow, 'unfollow'), 
        ))

        result = cursor.rowcount

        con.commit()
        db_util.close(con, cursor)

        print("*** new follow inserted")
        return result
