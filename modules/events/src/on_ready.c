#include "../include/on_ready.h"
#include <concord/log.h>

void on_ready(struct discord *client, const struct discord_ready *event) {
	  log_info("Client logged as: %s#%s",
           event->user->username,
           event->user->discriminator);
}
