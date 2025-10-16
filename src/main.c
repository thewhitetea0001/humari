#include <concord/discord.h>
#include <concord/log.h>
#include <string.h>

#define GUILD_ID 1428118894240862241
#define CONFIG_FILE "config.json"

void on_ready(struct discord *client, const struct discord_ready *event) {
  struct discord_create_guild_application_command params = {
    .name = "ping",
    .description = "Ping command!"
  };

  discord_create_guild_application_command(client, event->application->id,
                                           GUILD_ID, &params, NULL);
}

void on_interaction(struct discord *client, const struct discord_interaction *event) {
  if (event->type != DISCORD_INTERACTION_APPLICATION_COMMAND)
    return;

  if (strcmp(event->data->name, "ping") == 0) {
    struct discord_interaction_response params = {
      .type = DISCORD_INTERACTION_CHANNEL_MESSAGE_WITH_SOURCE,
      .data = &(struct discord_interaction_callback_data){
        .content = "pong"
      }
    };
    discord_create_interaction_response(client, event->id, event->token, &params, NULL);
  }
}

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
