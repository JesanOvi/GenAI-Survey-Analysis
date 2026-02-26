import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.patches as mpatches  # For patterns

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches
from scipy.signal import find_peaks

def grouped_bar_graph_horizontal_color(categories, cluster_1, cluster_2, cluster_3, cluster_4, cluster_5, title, w, h, legend_position='upper right'):
    # Combine data into a single array for the bars
    values = np.array([cluster_1, cluster_2, cluster_3, cluster_4, cluster_5])

    # Define legend labels and colors
    legend_val = ['Mech-Civil', 'CS-EE-AMS', 'Met-Geo-Pet', 'Phys-Chem', 'Society']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Distinct colors for the bars

    # Set bar height and position offsets
    bar_height = 0.17
    index = np.arange(len(categories))

    # Plot
    fig, ax = plt.subplots(figsize=(w, h)) # nor 10 6, 12 5.3 for usecase

    # Create the grouped horizontal bar chart with colors
    for i in range(len(values)):
        bars = ax.barh(index + i * bar_height, values[i], bar_height, color=colors[i], edgecolor='black', label=legend_val[i])

        # Add values at the end of each bar
        for bar in bars:
            width = bar.get_width()  # Get the width of the bar (for horizontal bars)
            ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2,  # Offset to the right of the bar
                    f'{width}', va='center', ha='left', color='black', rotation=0)

    # Adding labels and title
    #ax.set_xlabel('Frequency (Normalized)')
    #ax.set_title(title)
    ax.set_yticks(index + bar_height * 2)  # Move the y-ticks to the center of the group
    ax.set_yticklabels(categories, rotation=0)

    # Adjust the x-axis tick labels
    ax.tick_params(axis='x', labelsize=10)  # Set the font size for x-axis ticks
    
    # Increase the font size and wrap y-tick labels for categories
    ax.set_yticks(index + bar_height * 2)  # Move the y-ticks to the center of the group
    #wrapped_categories = [f'\n'.join(cat.split()) for cat in categories]  # Split and wrap text into multiple lines
    #ax.set_yticklabels(wrapped_categories, fontsize=8)  # Set font size for categories
    ax.set_yticklabels(categories, fontsize=14, fontweight='bold')  # Set font size for categories



    # Adding the legend (reversed order)
    reversed_legend_val = legend_val[::-1]
    reversed_colors = colors[::-1]
    handles = [mpatches.Patch(color=reversed_colors[i], label=reversed_legend_val[i]) for i in range(len(reversed_legend_val))]
    ax.legend(handles=handles, loc=legend_position)

    # Save the plot
    plt.tight_layout()
    add = '/Users/jesanahammed/Desktop/' + title
    plt.savefig(add, dpi=300)
    plt.show()



def stacked_bar_graph(categories, cluster_1, cluster_2, cluster_3, cluster_4, cluster_5, title):
    # Combine data into a single array for stacked bars
    values = np.array([cluster_1, cluster_2, cluster_3, cluster_4, cluster_5])

    legend_val = ['Mech-Civil', 'CS-EE-AMS', 'Met-Geo-Pet', 'Phys-Chem', 'Society']
    
    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create the stacked bar chart
    bars = ax.bar(categories, values[0], label='Mech-Civil')
    for i in range(1, len(values)):
        bars = ax.bar(categories, values[i], bottom=np.sum(values[:i], axis=0), label=legend_val[i])
    
    # Add values to each section of the bars
    for i, bar in enumerate(bars):
        y_offset = 0
        for j, section in enumerate(values):
            bar_height = section[i]
            ax.text(bar.get_x() + bar.get_width() / 2, y_offset + bar_height / 2,
                    f'{bar_height}', ha='center', va='center', color='white')
            y_offset += bar_height

    # Remove the code that displays the total value at the top of each bar
    #totals = np.sum(values, axis=0)
    #for i, total in enumerate(totals):
    #    ax.text(i, total + 2, f'{total}', ha='center', va='bottom')

    plt.xticks(rotation=45, ha="right")
    # Adding labels and title
    ax.set_ylabel('Frequency (Normalized)')
    ax.set_title(title)
    ax.legend()

    # Place the legend outside the plot
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    
    # Save the plot
    plt.tight_layout()
    add = '/Users/jesanahammed/Desktop/' + "" + title
    plt.savefig(add, dpi=300)
    plt.show()





def grouped_bar_graph_horizontal_color_white(categories, cluster_1, cluster_2, cluster_3, cluster_4, cluster_5, title, w, h, legend_position='upper right'):
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.patches as mpatches
    
    # Combine data into a single array for the bars
    values = np.array([cluster_1, cluster_2, cluster_3, cluster_4, cluster_5])

    # Define legend labels and colors
    legend_val = ['Mech-Civil', 'CS-EE-AMS', 'Met-Geo-Pet', 'Phys-Chem', 'Society']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Distinct colors for the bars

    # Set bar height and position offsets
    bar_height = 0.17
    index = np.arange(len(categories))

    # Plot
    fig, ax = plt.subplots(figsize=(w, h))

    # Create the grouped horizontal bar chart with colors
    for i in range(len(values)):
        bars = ax.barh(index + i * bar_height, values[i], bar_height, color=colors[i], edgecolor='black', label=legend_val[i])

        # Add values at the end of each bar
        for bar in bars:
            width = bar.get_width()  # Get the width of the bar (for horizontal bars)
            ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2,  # Offset to the right of the bar
                    f'{width}', va='center', ha='left', color='black', rotation=0)

    # Adding labels and title
    ax.set_yticks(index + bar_height * 2)  # Center the y-ticks
    wrapped_categories = [f'\n'.join(cat.split()) for cat in categories]  # Wrap text into multiple lines
    ax.set_yticklabels(wrapped_categories, fontsize=12, fontweight='bold')  # Set font size for categories

    # Adjust y-axis limits to eliminate extra space
    ax.set_ylim(index[0] - bar_height, index[-1] + bar_height * (len(values) + 1))

    # Adding the legend to the upper right corner inside the graph
    reversed_legend_val = legend_val[::-1]
    reversed_colors = colors[::-1]
    handles = [mpatches.Patch(color=reversed_colors[i], label=reversed_legend_val[i]) for i in range(len(reversed_legend_val))]
    ax.legend(handles=handles, loc='upper right', bbox_to_anchor=(1, 1), ncol=1, frameon=True)  # Adjust legend position

    # Adjust layout and save the plot
    plt.tight_layout(rect=[0, 0.03, 1, 1])  # Slight adjustment to remove top and bottom whitespace
    add = '/Users/jesanahammed/Desktop/' + title
    plt.savefig(add, dpi=300, bbox_inches='tight')
    plt.show()

def boxplot(custom_palette, df_new, departments_reversed):
    
    plt.figure(figsize=(6, 5))
    sns.boxplot(
        x='Department',
        y='Ethical_Score',
        data=df_new,
        palette=custom_palette,
        width=0.6,  # Adjust box width
        showmeans=True,  # Optional: Show mean as a diamond
        meanprops={"marker": "D", "markeredgecolor": "black", "markerfacecolor": "yellow"},
        order=departments_reversed  # Set custom order of departments
    )
    
    # Add titles and labels (optional, can customize)
    # plt.title('Department-wise Ethical Perspectives on GenAI', fontsize=16)
    plt.xlabel('', fontsize=14)
    plt.ylabel('', fontsize=14)
    
    # Make the department names bold
    plt.xticks(fontsize=11, fontweight='bold')
    plt.yticks(fontsize=12, fontweight='bold')
    
    # Layout adjustments for tight plotting
    plt.tight_layout()
    
    # Save the plot as an image
    add = '/Users/jesanahammed/Desktop/' + 'ethics'
    plt.savefig(add, dpi=300)
    
    # Show the plot
    plt.show()




def kde_plot(data, min, max, peak_pos, ytick, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    
    # KDE Plot with Clipping
    sns.kdeplot(data, clip=(min, max))
    plt.xlim(min, max)
    
    # Generate KDE data for finding peaks
    kde_data = sns.kdeplot(data, clip=(min, max)).get_lines()[0].get_data()
    x = kde_data[0]  # X values
    y = kde_data[1]  # Y values (density values)
    
    # Find peaks
    peaks, _ = find_peaks(y)  # Locate peaks in KDE curve
    
    # Plot the peaks on the KDE plot
    plt.plot(x[peaks], y[peaks], "ro")  # Mark peaks with red dots
    for peak in peaks:
        plt.text(x[peak], y[peak] + peak_pos,  # Offset slightly above the peak, 0.0001 for p(doom) estimation, 0.001 for others
                 f'{x[peak]:.2f}', ha='center', va='bottom', color='red', fontsize=35, fontweight='bold')  # Bigger peak values
    
    # Adjust x and y-axis ticks
    plt.tick_params(axis='both', labelsize=25)  # Make x and y-axis ticks bigger

    # Set x-axis ticks to range from 1 to 10
    #ticks = np.linspace(min, max-1, 11)  # Create 10 evenly spaced ticks # ticks for rating
    ticks = np.linspace(min, max, ytick)  # ticks for important of p(doom): 7, 10 for P(doom), 11 for others
    plt.xticks(ticks, labels=[f'{int(tick)}' for tick in ticks], fontsize=20)  # Format as integers and increase font size
    
    
    # Remove x and y labels
    plt.xlabel('')
    plt.ylabel('')

    #plt.savefig('/Users/jesanahammed/Desktop/impact_p(doom).png', dpi=300)
    
    # Show the plot
    address = '/Users/jesanahammed/Desktop/' + title
    plt.savefig(address, dpi=300)
    plt.show()
    
    # Print the peak values
    peak_values = x[peaks]
    print(f"Peak values are at: {peak_values}")


def heatmap_plot(categories1, categories2, residuals, xlabel, ylabel):
    # Create heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(residuals, annot=True, cmap="coolwarm", xticklabels=categories1, yticklabels=categories2, cbar=True)
    plt.title("Standardized Residuals Heatmap")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

