from crewai import Task
from agents import agents

research_task = Task(
    description=(
        "Research the latest trends and developments in {topic}."
        "Provide a detailed report summarizing the key points."
    ),
    expected_output='A detailed report with key points about the latest trends and developments in {topic}.',
    agent=agents['researcher']
)

write_task = Task(
    description=(
        "Write an article based on the research report provided."
        "Ensure the article is engaging and easy to understand."
    ),
    expected_output='An engaging article formatted as markdown with the key points about {topic}.',
    agent=agents['writer']
)

tasks = [research_task, write_task]
