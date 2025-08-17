


from dotenv import load_dotenv
# from livekit.agents import AutoAgent
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    noise_cancellation,
)
from prompt import instructions1,response_prompt                   

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=instructions1)


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
        model="gemini-2.0-flash-exp",
        voice="Kore",
        temperature=0.8,
        instructions=instructions1,
        )
    )
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions=response_prompt
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
