# Armanelo Bot - Development Repository

## Introduction

Welcome to the Armanelo development repository!  
Armanelo is a secure, developer-focused bot created by Trifonilix. It is designed with privacy, security, and exclusivity at its core. This repository is dedicated to enhancing the bot's capabilities while adhering to its core principles.

## Contribution Guidelines
TERST

### Pull Request Policy

- One pull request will be reviewed at a time.
- To ensure high-quality reviews and minimize conflicts, only one pull request will be active for review at any given time.
- Subsequent pull requests will remain in the queue until the active request is resolved.

### Workflow for Contributors

1. **Fork the Repository**:  
   Create a personal fork of this repository before making changes.
   
2. **Create a Feature Branch**:  
   Use descriptive branch names (e.g., `feature-new-logging-system` or `bugfix-database-issue`).

3. **Submit a Pull Request**:  
   Ensure your pull request is well-documented and adheres to the coding standards outlined below.  
   Include a summary of changes and any relevant details (e.g., why the change is necessary).

## Development Guidelines

### Core Principles

- **Privacy First**: Every feature must maintain the privacy of user data.
- **Security-Driven**: All additions must follow secure coding practices to protect sensitive data.

### Future Development Goals

- **Enhanced Logging System**: Implement modular logging to allow more detailed and customizable log management.
- **Advanced Whitelisting**: Add support for dynamic updates to the whitelist through a secure admin interface.
- **Developer Dashboard**: Create a web-based dashboard for collaborators to monitor system health, logs, and active pull requests.
- **Integration Testing**: Develop automated integration tests to ensure smooth compatibility with all supported platforms.

### Coding Standards

- Write clear and concise documentation for all functions, classes, and modules.
- Use meaningful commit messages and branch names.

## Priority Levels

To understand how different server levels are prioritized and what commands they can access, **scroll down** to the **Priority Levels** section. This section explains the distinctions between **Priority 1**, **Priority 2**, and **Priority 3** servers.

## Function Definitions

To view the list of bot functions used within Armanelo, **scroll down** to the section titled **Function Definitions**. This section outlines the key functions, their descriptions, and how they contribute to the bot’s operations.

Happy coding, and thank you for contributing to Armanelo!


<br>


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


<br>


# Priority Levels

## **Priority 1: Full Access**
- **Access Level**: All application commands
- **Description**: Priority 1 servers have the highest level of access, with permission to use all available commands, including the most critical commands. These servers have unrestricted control over the bot’s full functionality.

## **Priority 2: Limited Access**
- **Access Level**: Most commands, with some restrictions
- **Description**: Priority 2 servers have access to nearly all bot commands, but certain high-level commands are restricted. These servers are typically trusted, service-oriented environments that require access to most administrative and operational commands, but not those that would allow more extreme actions (e.g., forcing the bot to leave a server).

## **Priority 3: Basic Access**
- **Access Level**: Utility and miscellaneous commands
- **Description**: Priority 3 servers have the lowest access level. They are limited to using utility commands and other minor features that do not affect core bot functionality. These servers can perform basic tasks, but have no control over critical or administrative operations.

