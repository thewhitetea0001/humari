TARGET = ./main.out

INCLUDE_DIR = \
			modules/include

MODULES_SRC = \
			../modules/events/src/on_ready.c \
			../modules/commands/src/ping.c

SRC = \
			main.c

$(TARGET):
			gcc $(SRC) $(MODULES_SRC) -o $(TARGET) -pthread -ldiscord -lcurl
