TARGET = ./main.out

INCLUDE_DIR = \
			modules/include

MODULES_SRC = \
			../modules/events/src/on_ready.c \
			../modules/commands/src/ping.c \
			../modules/commands/src/kick.c \
			../modules/commands/src/on_interaction.c

SRC = \
			main.c

$(TARGET):
			gcc $(SRC) $(MODULES_SRC) -o $(TARGET) -pthread -ldiscord -lcurl
