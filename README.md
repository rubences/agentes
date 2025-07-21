# AI Tools Analysis and Visualization

This project provides visualization tools for analyzing AI chatbots and coding assistants, including Google Trends analysis and research figures for academic papers.

## Features

### Google Trends Analysis
- **ChatGPT**: OpenAI's conversational AI (launched November 2022)
- **Claude**: Anthropic's AI assistant (launched March 2022, gained popularity later)
- **Gemini**: Google's AI model (originally Bard in March 2023, rebranded December 2023)
- **Copilot**: GitHub's AI coding assistant (mainstream adoption from 2023)
- **Deepseek**: AI development platform (gained significant popularity in 2024)

### Research Figures
- Composite performance scores across Technical, Pedagogical, Ethical, and Psychological domains
- Ethical Compliance Index (ECI) comparison
- Perplexity (PPL) analysis with annotations
- Response Latency (RL) comparison with reference lines

## Installation

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Google Trends Visualization

Run the visualization script:

```bash
python google_trends_visualization.py
```

This will:
- Generate synthetic trends data
- Create and display the line chart
- Save the chart as `google_trends_spain_2022_2025.png`
- Export raw data as `google_trends_data.csv`

### Research Figures for AI Chatbot Comparison

Run the research figures script:

```bash
python research_figures.py
```

This will generate seven research figures:
- **Figure 1**: Composite scores by chatbot and domain (grouped bar chart)
- **Figure 2**: Ethical Compliance Index (ECI) by chatbot (vertical bar chart)
- **Figure 3**: Perplexity (PPL) by chatbot (bar chart with annotations)
- **Figure 4**: Response Latency (RL) by chatbot (bar chart with reference line)
- **Figure 5**: Student Satisfaction by chatbot (bar chart with error bars showing standard deviation)
- **Figure 6**: Use-Case-Specific Performance (grouped bar chart showing APA citation, ethical dilemmas, and multi-step reasoning)
- **Figure 7**: Correlation Matrix of Domain Scores (heatmap showing correlations between Technical, Pedagogical, Ethical, Psychological, and IoT Integration domains)

All figures are saved to the `data/` directory as high-resolution PNG files.

## Output

The scripts generate:

### Google Trends Visualization
- **PNG Chart**: High-resolution line chart showing trends over time
- **CSV Data**: Raw data points for further analysis
- **Console Output**: Summary statistics and data preview

### Research Figures
- **Figure1_CompositeScores.png**: Grouped bar chart comparing chatbots across four domains
- **Figure2_EthicalCompliance.png**: Vertical bar chart showing ECI scores
- **Figure3_Perplexity.png**: Bar chart with PPL values and annotations
- **Figure4_Latency.png**: Bar chart with response latency and reference line
- **Figure5_StudentSatisfaction.png**: Bar chart with student satisfaction scores and error bars showing standard deviations
- **Figure6_UseCasePerformance.png**: Grouped bar chart showing performance across APA citation tasks, ethical dilemma scenarios, and multi-step reasoning
- **Figure7_CorrelationMatrix.png**: Heatmap showing correlation matrix between domain scores (Technical, Pedagogical, Ethical, Psychological, IoT Integration)

## Data Methodology

The synthetic data is based on:
- Actual release dates of each AI tool
- Realistic adoption patterns observed in the market
- Spain-specific search behavior considerations
- Seasonal and trend variations

The popularity index ranges from 0-100, where 100 represents peak search interest relative to the highest point in the dataset for the given time period and location.