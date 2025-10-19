#include <concord/discord.h>
#include <concord/log.h>
#include <string.h>

// events
#include "../modules/events/include/on_ready.h"
// slash commands
#include "../modules/commands/include/commands.h"

#define GUILD_ID 1428118894240862241 // discord.gg/q3JPQE8NGD <3
#define CONFIG_FILE "config.json"

int main(void) {
  struct discord *client = discord_config_init(CONFIG_FILE);
  if (!client) {
    log_fatal("Failed to load CONFIG_FILE");
    return 1;
  }

  discord_set_on_ready(client, &on_ready);
  discord_set_on_interaction_create(client, &on_interaction);
  discord_run(client);

  return 0;
}
