# DELIMITER $$

# CREATE TRIGGER prevent_self_follows
#      BEFORE INSERT ON follows FOR EACH ROW
#      BEGIN
#           IF new.follower_id = NEW.followee_id
#           THEN
#               SIGNAL SQLSTATE '45000'
#                     SET MESSAGE_TEXT = 'Can not follow yourself!';
#           END IF;
#      END;
# $$
# DELIMITER ;

DELIMITER $$

CREATE TRIGGER capture_unfollow
     AFTER DELETE ON follows FOR EACH ROW
     BEGIN
          Insert into unfollows(follower_id, followee_id)
          values(old.follower_id, old.followee_id);
     END;
$$
DELIMITER ;

alter table test add check(age>17);

CREATE TABLE parts (
    part_no VARCHAR(18) PRIMARY KEY,
    description VARCHAR(40),
    cost DECIMAL(10,2 ) NOT NULL CHECK (cost >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0)
);