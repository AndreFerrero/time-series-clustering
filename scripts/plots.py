def pre_plots(groups, group_name: str):
    # Create an empty list to store modified dataframes
    dfs = []

    # Iterate through the dictionary values and groups labels
    for df, group in zip(datasets, groups):
        
        # Add a 'group' column
        df[group_name] = group
        
        # Append the modified dataframe to the list
        dfs.append(df)
    
    # Concatenate all dataframes in the list along the rows
    full_df = pd.concat(dfs, ignore_index=True)
    full_df
    
    return full_df

def plots(subfolder: str, vars, group):
    # subfolder should be a string indicating the name of the subfolder in the figures_folder
    # vars should be the list containing the variable names, therefore either pollutants, mets, numerics
    # group should be the variable we want to group by (eg: province, clusters,...)
    # to group we need to have created the full dataframe before with the specific group variable
    
    sns.set(style="whitegrid")

    figures_folder = R'C:\Users\andre\OneDrive - Alma Mater Studiorum Università di Bologna\University\UniBo\Machine Learning\PR2.20\figures'
    output_folder = os.path.join(figures_folder, subfolder)
    os.makedirs(output_folder, exist_ok=True)

    for var in vars:
        
        # Plot the time series for each province
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='date', y=var, hue=full_df[group], data=full_df)

        plt.title(f'Meteorological Information Over Time by {group}')
        plt.xlabel('Date')
        plt.ylabel(var)
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        
        save_path = os.path.join(output_folder, f'{var}.png')
        plt.savefig(save_path, bbox_inches='tight')
        
        plt.show()