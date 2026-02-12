from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class OpenbivWorkforce():
    """OpenbivWorkforce crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def project_intake_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['project_intake_agent'],
            verbose=True
        )

    @agent
    def market_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_agent'],
            verbose=True
        )

    @agent
    def project_planning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['project_planning_agent'],
            verbose=True
        )

    @task
    def intake_project_task(self) -> Task:
        return Task(
            config=self.tasks_config['intake_project_task'],
        )

    @task
    def research_project_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_project_task'],
        )

    @task
    def planning_project_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_project_task'],
            output_file='openbiv_project_plan.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the OpenbivWorkforce crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
