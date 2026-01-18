# Mining Agent

A comprehensive framework for demonstrating how process mining technology brings governance and observability to Agentic AI workflows. This project creates an AI-powered insurance verification agent and analyzes its execution patterns using advanced process mining techniques.

## Overview

This project demonstrates a complete AI agent lifecycle:
1. **Agent Creation**: Build an insurance coverage verification agent using Claude (Anthropic's AI)
2. **Workflow Execution**: Process patient queries with autonomous decision-making
3. **Process Mining**: Analyze agent behavior patterns, identify bottlenecks, and visualize workflow variants

### Key Features

- **Autonomous AI Agent**: Healthcare insurance verification agent with tool-calling capabilities
- **Process Mining Analysis**: Comprehensive workflow visualization and KPI tracking
- **Variant Analysis**: Identify different execution paths and their frequencies
- **Bottleneck Detection**: Automatically detect slow transitions and performance issues
- **Interactive Visualizations**: Dynamic workflow diagrams with Plotly and static diagrams with Matplotlib

## Project Structure

```
miningAgent/
├── Insurance_Verification_Agent.ipynb    # Agent creation and execution
├── Process_Mining.ipynb                  # Process mining analysis and visualization
├── Test.py                               # Test cases and edge case scenarios
├── environment.yml                       # Conda environment configuration
├── docs/                                 # Data files
│   ├── Medical Policy.docx               # Insurance policy document
│   ├── Patients.csv / Patients.xlsx      # 50 policyholder records
│   ├── Prompts.csv                       # 115 patient query prompts
│   └── agent_log.csv                     # Agent execution logs
└── README.md                             # This file
```

## Use Case: Insurance Coverage Verification

The AI agent handles healthcare insurance verification by:

1. **Patient Identification**: Verifying patient identity through ID, name, or surname
2. **Coverage Verification**: Checking if the patient's policy tier covers their medical needs
3. **Decision Making**: Providing clear coverage decisions (Covered/Not Covered/Escalated)

### Policy Tiers

- **Simple Membership** ($29.99/month): Basic medical and emergency services
- **Advanced Membership** ($79.99/month): Comprehensive care with preventative services
- **Premium Membership** ($149.99/month): Full coverage including specialized surgery

## Getting Started

### Prerequisites

- Python 3.12+
- Conda or Miniconda
- Anthropic API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/JPortilloHub/miningAgent.git
cd miningAgent
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate miningAgent-env
```

3. Set up your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Running the Agent

1. Open [Insurance_Verification_Agent.ipynb](Insurance_Verification_Agent.ipynb) in Jupyter
2. Run all cells to execute the agent on the 115 test prompts
3. Agent logs will be saved to `agent_log.csv`

### Running Process Mining Analysis

1. Open [Process_Mining.ipynb](Process_Mining.ipynb) in Jupyter
2. Run all cells to perform comprehensive process mining analysis
3. Generated outputs:
   - `agent_workflow_static.png` - Static workflow diagram
   - `agent_workflow_interactive.html` - Interactive workflow visualization
   - `variants_analysis.html` - Process variant analysis
   - `bottlenecks_analysis.html` - Bottleneck detection report

## Agent Architecture

### Tools

The agent has access to three core tools:

1. **verify_patient**: Validates patient identity against the database
2. **check_coverage**: Evaluates coverage based on policy tier and medical circumstance
3. **finalize_decision**: Records the final decision and closes the case

### Workflow

```
Coverage Inquiry → Input Message → Patient Verification → Coverage Check → Decision Finalized → Case Closed
```

The agent autonomously decides:
- When to request patient identification
- How to verify patient identity (ID, name, surname combinations)
- Whether the policy covers the requested service
- What decision to make (Covered/Not Covered/Escalated)

## Process Mining Capabilities

The `ProcessMiningTool` class provides:

### KPI Analysis
- Total cases and events
- Average/median case duration
- Activities per case
- Duration statistics (min, max, std dev)

### Workflow Visualization
- Hierarchical process flow diagrams
- Transition frequency and duration
- Node coloring by activity type (start, end, intermediate)
- Edge labels with timing metrics

### Variant Analysis
- Identification of unique execution paths
- Frequency and duration comparison
- Cumulative frequency analysis
- Top-N variant reporting

### Bottleneck Detection
- Automatic identification of slow transitions
- Duration variability analysis (Coefficient of Variation)
- Comparative performance metrics

## Example Test Cases

The project includes diverse test scenarios in [Test.py](Test.py):

- Patient with ID
- Patient without identification
- Patient with name only
- Patient with both ID and name (matching)
- Patient with ID and wrong name (validation test)
- Edge cases to test agent reasoning

## Dependencies

Core dependencies:
- `anthropic` - Claude AI API client
- `pandas` - Data manipulation
- `plotly` - Interactive visualizations
- `matplotlib` - Static visualizations
- `networkx` - Graph analysis
- `python-dotenv` - Environment variable management

See [environment.yml](environment.yml) for the complete list.

## Output Examples

### KPI Report
```
📊 PROCESS MINING KPI REPORT
═══════════════════════════════════════════════════════════
📁 Total Cases: 115
📋 Total Events: 575
📈 Avg Activities per Case: 5.0
⏱️  Case Duration Statistics:
   • Average:  2.5s
   • Median:   2.3s
   • Maximum:  8.7s
```

### Process Variants
The analysis identifies different execution paths, such as:
- Standard flow: Inquiry → Verification → Coverage Check → Decision → Close
- Retry flow: Inquiry → Failed Verification → Re-verification → Coverage Check → Decision → Close
- Escalation flow: Inquiry → Verification → Coverage Check → Escalated → Close

## License

This project is available for educational and demonstration purposes.
