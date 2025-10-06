class LearningSystem:
    def __init__(self, si_system: SyntheticIntelligenceSystem):
        self.si_system = si_system
        self.performance_data = []
        
    def record_performance(self, task_id: str, agent_id: str, success: bool, execution_time: float):
        self.performance_data.append({
            "task_id": task_id,
            "agent_id": agent_id,
            "success": success,
            "execution_time": execution_time
        })
    
    def optimize_agent_assignment(self):
        # Analyze performance data to improve future assignments
        agent_success_rates = {}
        for record in self.performance_data:
            agent_id = record["agent_id"]
            if agent_id not in agent_success_rates:
                agent_success_rates[agent_id] = []
            agent_success_rates[agent_id].append(record["success"])
        
        # Update agent capabilities based on performance
        for agent_id, successes in agent_success_rates.items():
            success_rate = sum(successes) / len(successes)
            print(f"Agent {agent_id} success rate: {success_rate:.2%}")

# Utility function for complex task decomposition
def decompose_complex_task(objective: str, max_subtasks: int = 10) -> List[str]:
    """Use AI to break down complex objectives (placeholder for actual AI integration)"""
    # In practice, you'd use an LLM here to intelligently decompose the task
    subtasks = [
        f"Understand and clarify: {objective}",
        f"Research relevant information for: {objective}",
        f"Analyze components of: {objective}",
        f"Develop solution approach for: {objective}",
        f"Implement core solution for: {objective}",
        f"Test and validate: {objective}",
        f"Document and present: {objective}"
    ]
    return subtasks[:max_subtasks]
