/* File info:
 * 		created: 25.10.19 14:40
 *		author: thewhitetea
*/

#include "../include/on_interaction.h"
#include "../include/kick.h"
#include "../include/ping.h"

#include <string.h>
#include <concord/log.h>

void on_interaction(struct discord *client, const struct discord_interaction *event) {
  if (event->type != DISCORD_INTERACTION_APPLICATION_COMMAND)
    return;

	const char *name = event->data->name;

  if (strcmp(name, "ping") == 0) {
    cmd_ping(client, event);
  } else if (strcmp(name, "kick") == 0) {
    cmd_kick(client, event);
  } else {
    log_warn("Unkow command: %s", name);
  }
}
