import disnake
import random
from disnake.ext import commands
from utilities.log import Log
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

class Work(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.engine = create_engine("sqlite:///databases/economydata.db", echo=False)
		self.Base = declarative_base()

		class User(self.Base):
			__tablename__ = "money"
			id = Column(Integer, primary_key=True)
			guild_id = Column(Integer)
			user_name = Column(String)
			user_id = Column(Integer)
			money = Column(Integer)

		self.User = User
		self.Base.metadata.create_all(self.engine)
		self.Session = sessionmaker(bind=self.engine)

	@commands.slash_command()
	@commands.cooldown(1, 7200, commands.BucketType.user)
	async def work(self, inter: disnake.ApplicationCommandInteraction):
		session = self.Session()
		try:
			Log.info("scmd", "work", f"({inter.author.name}) User used the command")

			income = random.randint(1, 4)
			user = session.query(self.User).filter_by(
				guild_id=inter.guild.id,  # Changed here
				user_id=inter.author.id
			).first()

			if user:
				user.money += income
				session.commit()
				Log.info("scmd", "work", f"({inter.author}) Added {income} money")
				await inter.response.send_message(f"Вы заработали {income} монеты! Теперь у вас **{user.money}** монет.")
			else:
				new_user = self.User(
					guild_id=inter.guild.id,  # Changed here
					user_name=str(inter.author),
					user_id=inter.author.id,
					money=income
				)
				session.add(new_user)
				session.commit()
				Log.info("scmd", "work", f"New user '{inter.author}' added with {income} money")
				await inter.response.send_message(f"Вы впервые заработали {income} монеты!")

		except Exception as e:
			await inter.response.send_message(f"Ошибка при выполнении команды:\n```sh\n{e}\n```", ephemeral=True)
			Log.error("scmd", "work", f"({inter.author.name}) {e}")
		finally:
			session.close()

def setup(client):
    client.add_cog(Work(client))