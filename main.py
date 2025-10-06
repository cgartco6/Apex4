async def main():
    # Initialize the synthetic intelligence system
    si_system = SyntheticIntelligenceSystem()
    
    # Register specialized agents
    si_system.register_agent(CoordinatorAgent("coordinator-1"))
    si_system.register_agent(ResearchAgent("research-1"))
    si_system.register_agent(AnalysisAgent("analysis-1"))
    si_system.register_agent(CreativeAgent("creative-1"))
    si_system.register_agent(TechnicalAgent("technical-1"))
    
    # Initialize workflow orchestrator
    orchestrator = WorkflowOrchestrator(si_system)
    
    # Start task manager
    task_manager = asyncio.create_task(si_system.task_manager())
    
    # Example complex task
    complex_objective = "Research and develop a comprehensive market analysis report for AI technology trends"
    
    print(f"🎯 Starting complex task: {complex_objective}")
    print("=" * 80)
    
    # Create workflow
    task_ids = orchestrator.create_complex_workflow(complex_objective)
    
    # Execute workflow
    await si_system.execute_workflow(task_ids)
    
    # Display results
    print("\n" + "=" * 80)
    print("📊 WORKFLOW COMPLETION REPORT")
    print("=" * 80)
    
    status_report = si_system.get_workflow_status()
    for task_id, task_info in status_report.items():
        status_icon = "✅" if task_info["status"] == "completed" else "❌"
        print(f"{status_icon} {task_info['description']}")
        print(f"   Agent: {task_info['assigned_agent']}")
        print(f"   Result: {task_info['result'][:100]}...")
        print()
    
    # Cancel task manager
    task_manager.cancel()

if __name__ == "__main__":
    asyncio.run(main())
