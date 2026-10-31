# conftest.py
import pytest
from dBot import createBot

@pytest.fixture
def simcord_bot():
    return createBot()

async def test_ping(simcord_env):
    channel = simcord_env.create_guild().create_text_channel("general")
    alice = simcord_env.guild.add_member(simcord_env.create_user("alice"))

    await alice.send(channel, "?ping")

    assert channel.last_message.content == "Pong!"
