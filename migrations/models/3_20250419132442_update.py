from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `chataimessagesession` DROP FOREIGN KEY `fk_chataime_user_8422bd56`;
        ALTER TABLE `chataimessage` DROP FOREIGN KEY `fk_chataime_chataime_3b5823f9`;
        ALTER TABLE `chataimessage` RENAME COLUMN `session_id_id` TO `session_id`;
        ALTER TABLE `chataimessagesession` RENAME COLUMN `user_id_id` TO `user_id`;
        ALTER TABLE `chataimessage` ADD CONSTRAINT `fk_chataime_chataime_2db1e123` FOREIGN KEY (`session_id`) REFERENCES `chataimessagesession` (`id`) ON DELETE CASCADE;
        ALTER TABLE `chataimessagesession` ADD CONSTRAINT `fk_chataime_user_f5f41a15` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `chataimessagesession` DROP FOREIGN KEY `fk_chataime_user_f5f41a15`;
        ALTER TABLE `chataimessage` DROP FOREIGN KEY `fk_chataime_chataime_2db1e123`;
        ALTER TABLE `chataimessage` RENAME COLUMN `session_id` TO `session_id_id`;
        ALTER TABLE `chataimessagesession` RENAME COLUMN `user_id` TO `user_id_id`;
        ALTER TABLE `chataimessage` ADD CONSTRAINT `fk_chataime_chataime_3b5823f9` FOREIGN KEY (`session_id_id`) REFERENCES `chataimessagesession` (`id`) ON DELETE CASCADE;
        ALTER TABLE `chataimessagesession` ADD CONSTRAINT `fk_chataime_user_8422bd56` FOREIGN KEY (`user_id_id`) REFERENCES `user` (`id`) ON DELETE CASCADE;"""
