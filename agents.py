import os
from dotenv import load_dotenv
from crewai import Agent
from crewai_tools import SerperDevTool

load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Create tools
search_tool = SerperDevTool()

# Define agents
researcher = Agent(
    role='Researcher',
    goal='Gather comprehensive information on {topic}',
    backstory=(
        "You are an experienced researcher with a knack for finding reliable and"
        "valuable information on any given topic."
    ),
    tools=[search_tool]
)

writer = Agent(
    role='Writer',
    goal='Compose an informative and engaging article on {topic}',
    backstory=(
        "You excel at crafting well-written articles that are both informative and"
        "engaging, making complex topics accessible to a wide audience."
    ),
    tools=[search_tool]
)

agents = {
    'researcher': researcher,
    'writer': writer
}