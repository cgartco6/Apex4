class WorkflowOrchestrator:
    def __init__(self, si_system: SyntheticIntelligenceSystem):
        self.si_system = si_system
        self.workflow_history = []
        
    def create_complex_workflow(self, objective: str) -> List[str]:
        """Break down complex objective into manageable tasks"""
        
        if "research" in objective.lower() and "report" in objective.lower():
            return self._create_research_workflow(objective)
        elif "develop" in objective.lower() or "build" in objective.lower():
            return self._create_development_workflow(objective)
        else:
            return self._create_general_workflow(objective)
    
    def _create_research_workflow(self, objective: str) -> List[str]:
        tasks = [
            self.si_system.create_task(f"Research background information for: {objective}"),
            self.si_system.create_task(f"Analyze research data for: {objective}"),
            self.si_system.create_task(f"Create outline for report on: {objective}", 
                                     dependencies=[0, 1]),
            self.si_system.create_task(f"Write detailed report on: {objective}", 
                                     dependencies=[2]),
            self.si_system.create_task(f"Review and finalize report on: {objective}", 
                                     dependencies=[3])
        ]
        return tasks
    
    def _create_development_workflow(self, objective: str) -> List[str]:
        tasks = [
            self.si_system.create_task(f"Analyze requirements for: {objective}"),
            self.si_system.create_task(f"Design architecture for: {objective}", 
                                     dependencies=[0]),
            self.si_system.create_task(f"Implement core functionality for: {objective}", 
                                     dependencies=[1]),
            self.si_system.create_task(f"Test and debug implementation for: {objective}", 
                                     dependencies=[2]),
            self.si_system.create_task(f"Document and deploy solution for: {objective}", 
                                     dependencies=[3])
        ]
        return tasks
    
    def _create_general_workflow(self, objective: str) -> List[str]:
        tasks = [
            self.si_system.create_task(f"Analyze and understand: {objective}"),
            self.si_system.create_task(f"Plan approach for: {objective}", dependencies=[0]),
            self.si_system.create_task(f"Execute primary work for: {objective}", dependencies=[1]),
            self.si_system.create_task(f"Review and refine results for: {objective}", dependencies=[2])
        ]
        return tasks
