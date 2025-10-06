import asyncio
import json
from typing import Dict, List, Any, Callable
from dataclasses import dataclass
from enum import Enum
import uuid
from abc import ABC, abstractmethod

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    id: str
    description: str
    dependencies: List[str]
    status: TaskStatus
    result: Any = None
    assigned_agent: str = None

class AIAgent(ABC):
    def __init__(self, agent_id: str, capabilities: List[str]):
        self.agent_id = agent_id
        self.capabilities = capabilities
        self.current_task = None
        
    @abstractmethod
    async def execute_task(self, task: Task) -> Any:
        pass

class SpecialistAgent(AIAgent):
    def __init__(self, agent_id: str, specialty: str, capabilities: List[str]):
        super().__init__(agent_id, capabilities)
        self.specialty = specialty
        
    async def execute_task(self, task: Task) -> Any:
        print(f"Agent {self.agent_id} ({self.specialty}) working on: {task.description}")
        await asyncio.sleep(1)  # Simulate work
        return f"Result from {self.specialty} agent for: {task.description}"

class CoordinatorAgent(AIAgent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, ["coordination", "delegation", "monitoring"])
        
    async def execute_task(self, task: Task) -> Any:
        return f"Coordinated task: {task.description}"

class SyntheticIntelligenceSystem:
    def __init__(self):
        self.agents: Dict[str, AIAgent] = {}
        self.tasks: Dict[str, Task] = {}
        self.task_queue = asyncio.Queue()
        self.results = {}
        
    def register_agent(self, agent: AIAgent):
        self.agents[agent.agent_id] = agent
        print(f"Registered agent: {agent.agent_id}")
        
    def create_task(self, description: str, dependencies: List[str] = None) -> str:
        task_id = str(uuid.uuid4())[:8]
        task = Task(
            id=task_id,
            description=description,
            dependencies=dependencies or [],
            status=TaskStatus.PENDING
        )
        self.tasks[task_id] = task
        return task_id
        
    def find_best_agent(self, task_description: str) -> AIAgent:
        # Simple matching - in reality, you'd use embeddings/ML
        description_lower = task_description.lower()
        
        for agent in self.agents.values():
            for capability in agent.capabilities:
                if capability in description_lower:
                    return agent
                    
        return list(self.agents.values())[0]  # Fallback
    
    async def process_task(self, task_id: str):
        task = self.tasks[task_id]
        
        # Check dependencies
        for dep_id in task.dependencies:
            if (dep_id not in self.results or 
                self.tasks[dep_id].status != TaskStatus.COMPLETED):
                print(f"Task {task_id} waiting for dependency {dep_id}")
                return
                
        # Assign to best agent
        agent = self.find_best_agent(task.description)
        task.assigned_agent = agent.agent_id
        task.status = TaskStatus.IN_PROGRESS
        
        try:
            result = await agent.execute_task(task)
            task.status = TaskStatus.COMPLETED
            task.result = result
            self.results[task_id] = result
            print(f"✅ Task completed: {task.description}")
        except Exception as e:
            task.status = TaskStatus.FAILED
            task.result = str(e)
            print(f"❌ Task failed: {task.description} - Error: {e}")
    
    async def task_manager(self):
        while True:
            task_id = await self.task_queue.get()
            await self.process_task(task_id)
            self.task_queue.task_done()
    
    async def execute_workflow(self, task_ids: List[str]):
        # Add tasks to queue
        for task_id in task_ids:
            await self.task_queue.put(task_id)
            
        # Wait for all tasks to complete
        await self.task_queue.join()
        
    def get_workflow_status(self):
        status = {}
        for task_id, task in self.tasks.items():
            status[task_id] = {
                "description": task.description,
                "status": task.status.value,
                "assigned_agent": task.assigned_agent,
                "result": task.result
            }
        return status
