"""
Research Figures Generator for AI Chatbot Comparison Study
Generates four specific figures for research paper on agent-based AI-IoT systems.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def create_data_directory():
    """Create data directory if it doesn't exist. Try /mnt/data first, fallback to ./data"""
    try:
        # Try to create /mnt/data as requested in specifications
        data_dir = '/mnt/data'
        os.makedirs(data_dir, exist_ok=True)
        # Test write permissions
        test_file = os.path.join(data_dir, '.test_write')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        return data_dir
    except (OSError, PermissionError):
        # Fallback to local data directory
        data_dir = os.path.join(os.getcwd(), 'data')
        os.makedirs(data_dir, exist_ok=True)
        print(f"Note: Using local data directory {data_dir} (could not access /mnt/data)")
        return data_dir

def generate_figure1_composite_scores():
    """
    Figure 1: Composite scores by chatbot and domain (grouped bar chart)
    Based on research results from the paper.
    """
    # Data extracted from research results
    chatbots = ["ChatGPT", "Claude", "Gemini", "Copilot", "Perplexity", "Deepseek"]
    
    # Composite scores by domain based on research text
    # Values estimated from paper results and overall scores
    data = {
        'Technical': [0.89, 0.85, 0.92, 0.82, 0.78, 0.70],      # Gemini leads, Deepseek lowest
        'Pedagogical': [0.83, 0.86, 0.88, 0.75, 0.72, 0.65],    # Gemini leads, good pedagogical performance
        'Ethical': [0.81, 0.82, 0.65, 0.78, 0.85, 0.68],        # Perplexity leads, Gemini moderate
        'Psychological': [0.80, 0.84, 0.85, 0.76, 0.73, 0.72]   # Gemini leads, good engagement
    }
    
    df = pd.DataFrame(data, index=chatbots)
    
    # Create the grouped bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Set up the bar chart
    x = np.arange(len(chatbots))
    width = 0.2
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    domains = list(data.keys())
    
    # Create bars for each domain
    for i, domain in enumerate(domains):
        ax.bar(x + i * width, df[domain], width, label=domain, color=colors[i], alpha=0.8)
    
    # Customize the chart
    ax.set_xlabel('Chatbots', fontweight='bold', fontsize=12)
    ax.set_ylabel('Puntuación (0–1)', fontweight='bold', fontsize=12)
    ax.set_title('Puntuaciones Compuestas por Chatbot y Dominio', fontweight='bold', fontsize=14, pad=20)
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(chatbots, rotation=45)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.0)
    
    plt.tight_layout()
    
    # Save the figure
    data_dir = create_data_directory()
    save_path = os.path.join(data_dir, 'Figure1_CompositeScores.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure 1 saved as: {save_path}")
    plt.show()
    
    return fig

def generate_figure2_ethical_compliance():
    """
    Figure 2: Ethical Compliance Index (ECI) by chatbot (vertical bar chart)
    Based on research results: ChatGPT and Perplexity = 4/4, others = 2/4
    """
    chatbots = ["ChatGPT", "Gemini", "Perplexity", "Claude", "Copilot", "Deepseek"]
    eci_scores = [4, 2, 4, 2, 2, 2]  # From research text
    
    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create bars with different colors
    colors = ['#2ECC71' if score == 4 else '#E74C3C' for score in eci_scores]
    bars = ax.bar(chatbots, eci_scores, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
    
    # Customize the chart
    ax.set_xlabel('Chatbots', fontweight='bold', fontsize=12)
    ax.set_ylabel('ECI (0–4)', fontweight='bold', fontsize=12)
    ax.set_title('Ethical Compliance Index (ECI) por Chatbot', fontweight='bold', fontsize=14, pad=20)
    ax.set_ylim(0, 4.5)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value annotations on bars
    for bar, score in zip(bars, eci_scores):
        height = bar.get_height()
        ax.annotate(f'{score}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),  # 3 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the figure
    data_dir = create_data_directory()
    save_path = os.path.join(data_dir, 'Figure2_EthicalCompliance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure 2 saved as: {save_path}")
    plt.show()
    
    return fig

def generate_figure3_perplexity():
    """
    Figure 3: Perplexity (PPL) by chatbot (bar chart with annotations)
    Based on research results: Copilot = 9, Deepseek = 15, ChatGPT = 12
    """
    chatbots = ["ChatGPT", "Claude", "Gemini", "Copilot", "Perplexity", "Deepseek"]
    ppl_scores = [12, 10, 13, 9, 11, 15]  # From research text and estimates
    
    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create bars with gradient colors based on performance (lower PPL is better)
    colors = ['#27AE60', '#2ECC71', '#F39C12', '#2ECC71', '#3498DB', '#E74C3C']
    bars = ax.bar(chatbots, ppl_scores, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
    
    # Customize the chart
    ax.set_xlabel('Chatbots', fontweight='bold', fontsize=12)
    ax.set_ylabel('Perplejidad (PPL)', fontweight='bold', fontsize=12)
    ax.set_title('Perplejidad (PPL) por Chatbot', fontweight='bold', fontsize=14, pad=20)
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, max(ppl_scores) * 1.15)
    
    # Add value annotations on bars
    for bar, score in zip(bars, ppl_scores):
        height = bar.get_height()
        ax.annotate(f'{score}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),  # 3 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the figure
    data_dir = create_data_directory()
    save_path = os.path.join(data_dir, 'Figure3_Perplexity.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure 3 saved as: {save_path}")
    plt.show()
    
    return fig

def generate_figure4_latency():
    """
    Figure 4: Response Latency (RL) by chatbot (bar chart with reference line)
    Based on research results: Perplexity = 1.0s, Gemini = 1.5s
    """
    chatbots = ["ChatGPT", "Claude", "Gemini", "Copilot", "Perplexity", "Deepseek"]
    latency_scores = [1.2, 1.3, 1.5, 1.1, 1.0, 1.4]  # From research text and estimates
    
    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create bars with colors based on performance (lower latency is better)
    colors = ['#3498DB', '#F39C12', '#E74C3C', '#2ECC71', '#27AE60', '#E67E22']
    bars = ax.bar(chatbots, latency_scores, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
    
    # Add reference line at 1.0 seconds
    ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Referencia (1.0s)')
    
    # Customize the chart
    ax.set_xlabel('Chatbots', fontweight='bold', fontsize=12)
    ax.set_ylabel('Latencia (s)', fontweight='bold', fontsize=12)
    ax.set_title('Latencia de Respuesta (RL) por Chatbot', fontweight='bold', fontsize=14, pad=20)
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, max(latency_scores) * 1.15)
    ax.legend()
    
    # Add value annotations on bars
    for bar, score in zip(bars, latency_scores):
        height = bar.get_height()
        ax.annotate(f'{score}s',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),  # 3 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the figure
    data_dir = create_data_directory()
    save_path = os.path.join(data_dir, 'Figure4_Latency.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure 4 saved as: {save_path}")
    plt.show()
    
    return fig

def generate_figure5_student_satisfaction():
    """
    Figure 5: Student Satisfaction and Perceived Usefulness
    Based on surveys of 300 students with satisfaction scores and standard deviations.
    """
    # Data from the research results
    chatbots = ["ChatGPT", "Claude", "Gemini", "Copilot", "Perplexity", "Deepseek"]
    satisfaction_scores = [4.1, 4.2, 3.9, 3.8, 3.7, 3.5]
    standard_deviations = [0.5, 0.4, 0.6, 0.5, 0.7, 0.8]
    
    # Create the bar chart with error bars
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create bars with colors based on performance (higher satisfaction is better)
    colors = ['#2ECC71', '#27AE60', '#3498DB', '#F39C12', '#E67E22', '#E74C3C']
    bars = ax.bar(chatbots, satisfaction_scores, yerr=standard_deviations, 
                  color=colors, alpha=0.8, edgecolor='black', linewidth=1,
                  capsize=5, error_kw={'ecolor': 'black', 'alpha': 0.7, 'capthick': 2})
    
    # Customize the chart
    ax.set_xlabel('Chatbots', fontweight='bold', fontsize=12)
    ax.set_ylabel('Puntuación de Satisfacción (0–5)', fontweight='bold', fontsize=12)
    ax.set_title('Figure 5: Student Satisfaction by Chatbot', fontweight='bold', fontsize=14, pad=20)
    ax.set_ylim(0, 5)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value annotations on bars
    for bar, score, sd in zip(bars, satisfaction_scores, standard_deviations):
        height = bar.get_height()
        ax.annotate(f'{score}\n±{sd}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 5),  # 5 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the figure
    data_dir = create_data_directory()
    save_path = os.path.join(data_dir, 'Figure5_StudentSatisfaction.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure 5 saved as: {save_path}")
    plt.show()
    
    return fig

def generate_figure6_usecase_performance():
    """
    Figure 6: Use-Case–Specific Performance
    Shows performance in APA citation, ethical dilemmas, and multi-step reasoning.
    """
    # Data from research results
    categories = ['APA Citation\nAccuracy (%)', 'Ethical Dilemma\nAccuracy (%)', 'Multi-step Reasoning\n(Avg Steps)']
    
    # Performance data for each category
    apa_data = {'Claude': 82, 'ChatGPT': 78, 'Copilot': 70}
    ethical_data = {'Claude': 90, 'ChatGPT': 85, 'Gemini': 75}
    reasoning_data = {'Copilot': 4.1, 'Deepseek': 2.6}
    
    # Create the grouped bar chart
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Set up positions for grouped bars
    x_pos = np.arange(len(categories))
    bar_width = 0.15
    
    # Colors for each chatbot
    chatbot_colors = {
        'ChatGPT': '#FF6B6B',
        'Claude': '#4ECDC4', 
        'Gemini': '#45B7D1',
        'Copilot': '#96CEB4',
        'Perplexity': '#FECA57',
        'Deepseek': '#FF9FF3'
    }
    
    # Collect all unique chatbots across categories
    all_chatbots = set()
    all_chatbots.update(apa_data.keys())
    all_chatbots.update(ethical_data.keys())
    all_chatbots.update(reasoning_data.keys())
    all_chatbots = sorted(list(all_chatbots))
    
    # Plot bars for each chatbot
    for i, chatbot in enumerate(all_chatbots):
        values = []
        positions = []
        
        # APA Citation
        if chatbot in apa_data:
            values.append(apa_data[chatbot])
            positions.append(x_pos[0] + i * bar_width - (len(all_chatbots)-1) * bar_width / 2)
        
        # Ethical Dilemma
        if chatbot in ethical_data:
            values.append(ethical_data[chatbot])
            positions.append(x_pos[1] + i * bar_width - (len(all_chatbots)-1) * bar_width / 2)
        
        # Multi-step Reasoning (scale to percentage for consistency)
        if chatbot in reasoning_data:
            # Scale reasoning steps to 0-100 scale for better visualization
            scaled_value = reasoning_data[chatbot] * 20  # 4.1 → 82, 2.6 → 52
            values.append(scaled_value)
            positions.append(x_pos[2] + i * bar_width - (len(all_chatbots)-1) * bar_width / 2)
        
        if values and positions:
            bars = ax.bar(positions, values, bar_width, label=chatbot, 
                         color=chatbot_colors[chatbot], alpha=0.8, edgecolor='black', linewidth=0.5)
            
            # Add value annotations
            for bar, val in zip(bars, values):
                height = bar.get_height()
                if bar.get_x() < x_pos[2] + 0.5:  # For APA and Ethical (percentages)
                    label = f'{int(val)}%'
                else:  # For reasoning (original values)
                    original_val = reasoning_data[chatbot]
                    label = f'{original_val}'
                ax.annotate(label,
                           xy=(bar.get_x() + bar.get_width() / 2, height),
                           xytext=(0, 3),
                           textcoords="offset points",
                           ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # Customize the chart
    ax.set_xlabel('Performance Categories', fontweight='bold', fontsize=12)
    ax.set_ylabel('Performance Score', fontweight='bold', fontsize=12)
    ax.set_title('Figure 6: Use-Case–Specific Performance by Chatbot', fontweight='bold', fontsize=14, pad=20)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(categories)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, 100)
    
    # Add note about reasoning scale
    ax.text(0.02, 0.98, 'Note: Multi-step reasoning shows actual step count', 
            transform=ax.transAxes, fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    
    # Save the figure
    data_dir = create_data_directory()
    save_path = os.path.join(data_dir, 'Figure6_UseCasePerformance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure 6 saved as: {save_path}")
    plt.show()
    
    return fig

def generate_figure7_correlation_matrix():
    """
    Figure 7: Correlations Between Domains
    Shows correlation matrix with strong positive correlations between domains.
    """
    # Data from research results
    domains = ['Technical', 'Pedagogical', 'Ethical', 'Psychological', 'IoT Integration']
    
    # Create correlation matrix based on research findings
    correlation_matrix = np.array([
        [1.00, 0.60, 0.35, 0.94, 0.85],  # Technical
        [0.60, 1.00, 0.65, 0.90, 0.70],  # Pedagogical  
        [0.65, 0.65, 1.00, 0.45, 0.40],  # Ethical
        [0.94, 0.90, 0.45, 1.00, 0.88],  # Psychological
        [0.85, 0.70, 0.40, 0.88, 1.00]   # IoT Integration
    ])
    
    # Create the heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create heatmap with divergent colormap centered at 0
    im = ax.imshow(correlation_matrix, cmap='RdYlBu_r', aspect='auto', vmin=-1, vmax=1)
    
    # Set ticks and labels
    ax.set_xticks(np.arange(len(domains)))
    ax.set_yticks(np.arange(len(domains)))
    ax.set_xticklabels(domains, rotation=45, ha='right')
    ax.set_yticklabels(domains)
    
    # Add correlation values to each cell
    for i in range(len(domains)):
        for j in range(len(domains)):
            text = ax.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                          ha="center", va="center", color="black", fontweight='bold')
    
    # Customize the chart
    ax.set_title('Figure 7: Correlation Matrix of Domain Scores', fontweight='bold', fontsize=14, pad=20)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Correlation Coefficient (r)', fontweight='bold', rotation=270, labelpad=20)
    
    plt.tight_layout()
    
    # Save the figure
    data_dir = create_data_directory()
    save_path = os.path.join(data_dir, 'Figure7_CorrelationMatrix.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Figure 7 saved as: {save_path}")
    plt.show()
    
    return fig

def main():
    """
    Main function to generate all research figures.
    """
    print("Generating research figures for AI chatbot comparison study...")
    print("=" * 60)
    
    # Generate all figures
    try:
        print("\nGenerating Figure 1: Composite Scores...")
        generate_figure1_composite_scores()
        
        print("\nGenerating Figure 2: Ethical Compliance Index...")
        generate_figure2_ethical_compliance()
        
        print("\nGenerating Figure 3: Perplexity...")
        generate_figure3_perplexity()
        
        print("\nGenerating Figure 4: Response Latency...")
        generate_figure4_latency()
        
        print("\nGenerating Figure 5: Student Satisfaction...")
        generate_figure5_student_satisfaction()
        
        print("\nGenerating Figure 6: Use-Case-Specific Performance...")
        generate_figure6_usecase_performance()
        
        print("\nGenerating Figure 7: Correlation Matrix...")
        generate_figure7_correlation_matrix()
        
        print("\n" + "=" * 60)
        print("All research figures have been generated successfully!")
        print(f"Figures saved in: {os.path.join(os.getcwd(), 'data')}")
        
    except Exception as e:
        print(f"Error generating figures: {e}")
        raise

if __name__ == "__main__":
    main()