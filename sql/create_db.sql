-- user(root)
create database my_purpose;

-- GRANT ALL PRIVILEGES ON `my_purpose`.* TO `jh`@`%`

-- user(jh)

CREATE TABLE mt_users(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    profile VARCHAR(2000) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id), 
    UNIQUE KEY email (email)
);

CREATE TABLE mt_users_follow_list(
    user_id INT NOT NULL,
    follow_user_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (user_id, follow_user_id),
    CONSTRAINT users_follow_list_user_id_fkey FOREIGN KEY (user_id) REFERENCES mt_users(id), 
    CONSTRAINT users_follow_list_follow_user_id_fkey FOREIGN KEY (follow_user_id) REFERENCES mt_users(id)
);

CREATE TABLE mt_tweets(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    tweet VARCHAR(300) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id),
    CONSTRAINT tweets_user_id_fkey FOREIGN KEY (user_id) REFERENCES mt_users(id)
);

