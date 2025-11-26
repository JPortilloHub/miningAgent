    all_logs = []   

    Example 1: Patient asks about coverage with identification
    print("\n### EXAMPLE 1: Patient with ID ###")
    logs1 = run_coverage_agent(
        "Hi, I'm patient ID 3. I need to know if my policy covers specialized surgery?"
    )
    all_logs.extend(logs1)

    print("\n### EXAMPLE 2: Patient without identification ###")
    logs2 = run_coverage_agent(
        "I need to know if my insurance covers dental work."
    )
    all_logs.extend(logs2)

    print("\n### EXAMPLE 3: Patient with name ###")
    logs3 = run_coverage_agent(
        "This is Alice Johnson. Am I covered for preventative care and annual physicals?"
    )
    all_logs.extend(logs3)

    print("\n### EXAMPLE 4: Patient with name ###")
    logs4 = run_coverage_agent(
        "I'm patient ID 3 and my name is Antonio Perico. Am I covered for preventative care and annual physicals?"
    )
    all_logs.extend(logs4)

     print("\n### EXAMPLE 4: Patient with name ###")
    logs5 = run_coverage_agent(
        "I'm patient ID 8 and I have a bacterial infection. Am I covered for the 6 month treatment of antibiotic?"
    )
    all_logs.extend(logs5)

    print("\n### EXAMPLE 6: Patient with correct ID but wrong name (should fail) ###")
    logs6 = run_coverage_agent(
        "Hi, I'm patient ID 3, my name is John Smith. Do you cover dental?"
    )
    all_logs.extend(logs6)

    print("\n### EXAMPLE 7: Patient with all correct attributes ###")
    logs7 = run_coverage_agent(
        "Hi, I'm patient ID 1, Alice Johnson. Am I covered for telemedicine?"
    )
    all_logs.extend(logs7)

    Print summary of all logs
    print("\n" + "="*60)
    print("COMPLETE LOG SUMMARY")

    for log in all_logs:
        print(json.dumps(log, indent=2))