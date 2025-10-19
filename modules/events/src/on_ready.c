#include "../include/on_ready.h"
#include <concord/log.h>

#define GUILD_ID 1428118894240862241 // discord.gg/q3JPQE8NGD <3

void on_ready(struct discord *client, const struct discord_ready *event) {
	  log_info("Client logged as: %s#%s",
           event->user->username,
           event->user->discriminator);

		struct discord_create_guild_application_command cmd_ping = {
			.name = "ping",
			.description = "Ответит Pong!"
		};
		log_info("Command \"/ping\" has been successfully registered");

		struct discord_create_guild_application_command cmd_kick = {
			.name = "kick",
			.description = "Кикнуть пользователя"
		};
		log_info("Command \"/kick\" has been successfully registered");

		const u64snowflake guild_id = GUILD_ID;

		discord_create_guild_application_command(client, event->application->id, guild_id, &cmd_ping, NULL);
		discord_create_guild_application_command(client, event->application->id, guild_id, &cmd_kick, NULL);
}
