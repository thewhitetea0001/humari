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
            Log.info("scmd", "work", f"({inter.author.name}) User used the command")

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
                Log.info("srcmd", "work", f"({inter.author}) Successfully added {icome_count} money")
                await inter.response.send_message(f"Вы заработали {icome_count} монетки! Теперь у вас **{user.money}** монеток!")
            else:
                Log.warn("scmd", "work", f"Uknow user '{inter.author}'")
                new_user = User(
                    name=str(inter.author),
                    user_id=int(inter.author.id),
                    money=2
                )
                session.add(new_user)
                session.commit()
                Log.info("scmd", "work", f"Successfully added new user '{inter.author}' ({inter.author.id}) to the economy table")
                await inter.response.send_message("Вы впервые заработали 2 монетки!")
        except Exception as e:
            await inter.response.send_message(f"Ошибка при выполнении команды:\n```sh\n{e}\n```", ephemeral=True)
            Log.error("scmd", "work", f"({inter.author.name}) e")

def setup(client):
    client.add_cog(Work(client))