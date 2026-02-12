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
    def sales_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['sales_agent'],
            verbose=True
        )

    @agent
    def content_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['content_agent'],
            verbose=True
        )

    @agent
    def cskh_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['cskh_agent'],
            verbose=True
        )

    @task
    def sales_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['sales_strategy_task'],
        )

    @task
    def content_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_plan_task'],
        )

    @task
    def cskh_playbook_task(self) -> Task:
        return Task(
            config=self.tasks_config['cskh_playbook_task'],
            output_file='openbiv_workforce_output.md'
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
