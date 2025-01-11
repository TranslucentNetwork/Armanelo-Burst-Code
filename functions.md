# Armanelo Bot - Function Definitions

## Database Functions

### `async serviceowner()`
Retrieves a list of `discord_id` from the `serviceowner` table in the database. This function is used to identify server/service owners, who are granted second-level priority for certain commands. They hold the second-highest level of action.

### `async getdevs()`
Fetches a list of `discord_id` from the `developers` table in the database. This function is used to identify developers, who have access to developer-specific commands and hold the second level of action within the system.

### `async getops()`
Retrieves a list of `discord_id` from the `operators` table in the database. Operators hold the highest level of action, and this function is used to manage their commands and privileges.

### `async setlog(guild_id, channel_id, category)`
Inserts a new record into the `logging` table with the specified `guild_id`, `channel_id`, and `category`. This function logs channel-specific details for later retrieval.

### `async getrecord(guild_id, category)`
Fetches a `channel_id` from the `logging` table based on the provided `guild_id` and `category`. This function is useful for retrieving stored logging information.

### `async removelog(guild_id, category)`
Deletes a record from the `logging` table for the specified `guild_id` and `category`. This function is used for log management and cleanup.

### `async changelog(guild_id, channel_id, category)`
Updates the `channel_id` in the `logging` table for the given `guild_id` and `category`. This function allows modification of existing logging records.

### `async get_channel(guild_id, channel_id, category)`
Fetches the `channel_id` from the `logging` table based on the `guild_id` and `category`. This function is useful when checking for a channel's logging configuration.

### `async logunique(guild_id, channel_id, category)`
Checks the uniqueness of a log entry for a given `channel_id` and `category` in the `logging` table. This function is used to ensure no duplicate log entries exist for the same category.

### `async getlog(guild_id, category)`
Retrieves the `channel_id` from the `logging` table for the provided `guild_id` and `category`. If no record exists, it returns a default response indicating no configuration.

### `async logban(moderator, user, reason)`
Inserts a record into the `gban` table, logging a ban action for a specified `user`, `moderator`, and `reason`. This function is used to track global bans and related information.

### `async getban(user)`
Fetches the ban `reason` for a specified `user` from the `gban` table. This function is used to retrieve information about a user's global ban status.

---

## Notes:

- All functions manage database connections and execute queries on relevant tables, including `serviceowner`, `developers`, `operators`, `logging`, and `gban`.
- These functions use `async` to perform non-blocking database operations, ensuring efficient execution.
- Comprehensive exception handling has been implemented to capture and log errors during database interactions, ensuring robust performance.
