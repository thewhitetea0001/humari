import disnake
import random
from disnake.ext import commands
from utilities.log import Log
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

class Work(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def work(
        self, 
        inter: disnake.ApplicationCommandInteraction
    ):
        try:
            Log.info(f"User {inter.author.name} has used the '/work' command")

            icome_count = random.randint(1, 5)

            engine = create_engine("sqlite:///databases/economydata.db", echo=False)

            Base = declarative_base()

            class User(Base):
                __tablename__ = "money"
                id = Column(Integer, primary_key=True)
                name = Column(String)
                user_id = Column(Integer)
                money = Column(Integer)
            
            Base.metadata.create_all(engine)

            Session = sessionmaker(bind=engine)
            session = Session()

            user = session.query(User).filter_by(user_id=inter.author.id).first() # there is user_id

            if user: # find user by user_id
                user.money += icome_count
                session.commit()
                await inter.response.send_message(f"Вы заработали {icome_count} монетки! Теперь у вас **{user.money}** монеток!")
            else:
                Log.warn(f"work: Uknow user '{inter.author}'")
                new_user = User(
                    name=str(inter.author),
                    user_id=int(inter.author.id),
                    money=2
                )
                session.add(new_user)
                session.commit()
                Log.info(f"work: Successull added new user '{inter.author}' ({inter.author.id}) to the economy table")
                await inter.response.send_message("Вы впервые заработали 2 монетки!")
        except Exception as e:
            await inter.response.send_message(f"Ошибка при выполнении команды:\n```sh\n{e}\n```", ephemeral=True)
            Log.error(f"({inter.author.name}) work", e)

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.CommandOnCooldown):
            await inter.response.send_message(f"Пожалуйста, подождите {error.retry_after:.1f} сек. ({int(error.retry_after/60)} мин.)", ephemeral=True)
            Log.warn(f"({inter.author}) work: The user has exceeded command usage limit")
        else:
            Log.error(f"({inter.author}) work", error)

def setup(client):
    client.add_cog(Work(client))