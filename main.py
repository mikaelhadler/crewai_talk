from crewai import Crew, Process
from tasks import tasks
from agents import agents

def run_crew(topic):
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential
    )

    result = crew.kickoff(inputs={'topic': topic})
    print(crew.usage_metrics)
    return result
