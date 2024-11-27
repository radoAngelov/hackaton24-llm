import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai_tools import SerperDevTool
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff

os.environ["SERPER_API_KEY"] = "b4c42df824647879625f4c45fbfd9092368999f6"

@CrewBase
class CompanyDataExtraction():
	"""CompanyDataExtraction crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	azure_llm = LLM(
		model="azure/gpt-4o-mini",
		base_url="https://dext-hackathon-swedencentral.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview",
		api_key="ExV3w4QhW8J638T5RMGAik6n74heIn0MLILDD2zI5U2bfXBtP5GeJQQJ99AKACfhMk5XJ3w3AAABACOGzvn0",
	)

	@after_kickoff
	def log_results(self, output):
		# Example of logging results, dynamically changing the output
		print(f"Results: {output}")
		return output

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			llm=self.azure_llm,
			verbose=True,
			tools=[SerperDevTool(country="uk", locale="en")]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			llm=self.azure_llm,
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CompanyDataExtraction crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
