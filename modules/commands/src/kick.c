/* File info:
 * 		created: 25.10.19 14:36
 *		author: thewhitetea
*/

#include "../include/kick.h"
#include <concord/discord.h>
#include <concord/log.h>

void cmd_kick(struct discord *client, const struct discord_interaction *event) {
	struct discord_interaction_response params = {
		.type = DISCORD_INTERACTION_CHANNEL_MESSAGE_WITH_SOURCE,
		.data = &(struct discord_interaction_callback_data){
			.content = "> Команда в разработка :с"
		}
	};
	discord_create_interaction_response(client, event->id,
																				event->token, &params, NULL);

	const char *username = event->member->user->username;
	log_info("The command /kick has used by %s", username);
}
