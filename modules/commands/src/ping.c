#include "../include/commands.h"
#include <concord/log.h>
#include <string.h>

void on_interaction(struct discord *client, const struct discord_interaction *event) {
	if (event->type != DISCORD_INTERACTION_APPLICATION_COMMAND)
		return; // return if interaction isn't a slash command :3
	
	// ping command
	if (strcmp(event->data->name, "ping") == 0) {
		struct discord_interaction_response params = {
			.type = DISCORD_INTERACTION_CHANNEL_MESSAGE_WITH_SOURCE,
			.data = &(struct discord_interaction_callback_data){
				.content = "https://tenor.com/view/toad-pet-pet-frog-petting-gif-17558648" // a tennor gif
			}
		};
		discord_create_interaction_response(client, event->id,
																					event->token, &params, NULL);
	}
}
