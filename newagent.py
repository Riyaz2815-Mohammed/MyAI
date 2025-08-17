from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    noise_cancellation,
)
from prompt import instructions1, response_prompt

load_dotenv()


# Custom AI Agent definition
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=instructions1)


async def entrypoint(ctx: agents.JobContext):
    # Initialize a session with Google Gemini Realtime model
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Puck",           # AI voice output
            temperature=0.8,
            instructions=instructions1,
        )
    )

    # Print whenever AI sends a message
    @session.event("message")
    async def on_message(ev: agents.MessageEvent):
        if ev.text:
            print("\n[AI Response]:", ev.text, "\n")

    # Start the session with our Assistant agent
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # First reply from the AI (startup greeting)
    await session.generate_reply(
        instructions=response_prompt
    )


if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
