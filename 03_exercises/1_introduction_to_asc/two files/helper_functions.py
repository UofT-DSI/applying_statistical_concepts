import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


def plot_temperature_vs_ice_cream_sales():
    """
    Generate and plot a linear regression model for temperature vs ice cream sales.
    """
    # Generate some made-up data
    np.random.seed(0)
    temperatures = np.random.uniform(60, 100, 500)  # Randomly choose temperatures between 60 and 100 degrees
    ice_cream_sales = temperatures * 1.5 + np.random.normal(0, 10, 500)  # Randomly (kinda) choose sales made

    # Reshape the temperatures for sklearn
    temperatures_reshaped = temperatures.reshape(-1, 1)

    # Create a linear regression model
    model = LinearRegression()
    model.fit(temperatures_reshaped, ice_cream_sales)
    predictions = model.predict(temperatures_reshaped)

    # Plot the graph
    scatter_plot(
        X={'data': [temperatures, ice_cream_sales], 'color': 'blue', 'label': 'Ice Cream Sales'}, 
        line_plot={'x': temperatures, 'y': predictions, 'color': 'red', 'linestyle': '--'},
        title='Temperature vs Ice Cream Sales',
        show_legend=True,
        xlabel='Temperature (°F)',
        ylabel='Ice Cream Sales'
    )


def sleep_and_study():
    """
    Generate and plot a logistic regression model for hours studied and hours slept vs pass/fail outcome.
    """
    # Generate sample data: Hours studied, hours of sleep, and pass/fail outcomes
    np.random.seed(42)
    hours_studied = np.random.uniform(1, 10, 500)
    hours_sleep = np.random.uniform(4, 10, 500)
    pass_fail = (hours_studied + hours_sleep > 12).astype(int)

    # Fit the regression model
    study_sleep_data = np.column_stack((hours_studied, hours_sleep))
    model = LogisticRegression()
    model.fit(study_sleep_data, pass_fail)

    # Line Plot Coordinates
    x_values = np.linspace(0, 12, 300)
    y_values = -(model.intercept_ + model.coef_[0][0] * x_values) / model.coef_[0][1]

    # Defining benign data and malignant data
    benign_data = [hours_studied[pass_fail == 0], hours_sleep[pass_fail == 0], "Fail"]
    malignant_data = [hours_studied[pass_fail == 1], hours_sleep[pass_fail == 1], "Pass"]
    
    # Plot the graph
    scatter_plot(
        X={'data': [benign_data[0], benign_data[1]], 'color': 'red', 'label': 'Fail'}, 
        y={'data': [malignant_data[0], malignant_data[1]], 'color': 'green', 'label': 'Pass'}, 
        line_plot={'x': x_values, 'y': y_values, 'color': 'blue', 'linestyle': '--'},
        title='Logistic Regression: Decision Boundary', 
        show_legend=False
    )

def plot_distribution(data, x, title, xlabel, ylabel, xticks_labels):
    """
    Plot the distribution of a categorical variable.

    Parameters:
    data (DataFrame): The dataset.
    x (str): The column to plot.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    xticks_labels (list): The labels for the x-ticks.
    """

    plt.figure(figsize=(6, 4))
    sns.countplot(x=x, data=data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(ticks=[0, 1], labels=xticks_labels)
    plt.show()

def plot_heatmap(matrix, title, xlabel, ylabel, xticklabels, yticklabels, cmap='Blues'):
    """
    Plot a heatmap.

    Parameters:
    matrix (array): The data to plot.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    xticklabels (list): The labels for the x-ticks.
    yticklabels (list): The labels for the y-ticks.
    cmap (str): The color map to use for the heatmap.
    """
    plt.figure(figsize=(6, 4))
    sns.heatmap(matrix, annot=True, fmt='d', cmap=cmap, cbar=False, xticklabels=xticklabels, yticklabels=yticklabels)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def print_report(y_true, y_pred, target_names):
    """
    Print a classification report.

    Parameters:
    y_true (array): The true labels.
    y_pred (array): The predicted labels.
    target_names (list): The names of the target classes.
    """
    print("Classification Report:")
    print(classification_report(y_true, y_pred, target_names=target_names)) 


def scatter_plot(X, y=None, line_plot=None, title='', show_legend=True, xlabel='', ylabel=''):
    """
    Create a scatter plot with optional labels, decision boundary, and filled areas.

    Parameters:
    X (dict): The data for the first class with keys 'data', 'color', and 'label'.
    y (dict, optional): The data for the second class with keys 'data', 'color', and 'label'.
    line_plot (dict, optional): The line plot details with keys 'x', 'y', 'color', 'linestyle', 'fill_colors', and 'model'.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    ylim (tuple, optional): The limits for the y-axis.
    show_legend (bool, optional): Whether to show the legend.
    """
    plt.figure(figsize=(8, 6))

    # Plotting the data points for X
    plt.scatter(X['data'][0], X['data'][1], color=X['color'], label=X["label"], edgecolors='k')
    
    # Plotting the data points for y, if provided
    if y is not None:
        plt.scatter(y['data'][0], y['data'][1], color=y['color'], label=y["label"], edgecolors='k')

    # Determining the ylim
    all_y_values = X['data'][1]
    if y is not None:
        all_y_values = np.concatenate([all_y_values, y['data'][1]])
    if line_plot is not None:
        all_y_values = np.concatenate([all_y_values, line_plot["y"]])

    y_min, y_max = all_y_values.min(), all_y_values.max()
    y_range = y_max - y_min
    y_extension = y_range * 0.1  # 10% extension
    ylim = y_min - y_extension, y_max + y_extension
    plt.ylim(ylim)

    # Plotting the line plot
    if line_plot is not None:
        plt.plot(line_plot['x'], line_plot['y'], color=line_plot['color'], linestyle=line_plot['linestyle'], label='Decision Boundary')

        if 'fill_colors' in line_plot and ylim is not None:
            point_above = np.array([[line_plot['x'][0], line_plot['y'][0] + 1]])
            prediction_above = line_plot['model'].predict(point_above) if 'model' in line_plot else None

            if prediction_above == 1:
                plt.fill_between(line_plot['x'], line_plot['y'], ylim[1], color=line_plot['fill_colors'][1], alpha=0.2)
                plt.fill_between(line_plot['x'], ylim[0], line_plot['y'], color=line_plot['fill_colors'][0], alpha=0.2)
            else:
                plt.fill_between(line_plot['x'], line_plot['y'], ylim[1], color=line_plot['fill_colors'][0], alpha=0.2)
                plt.fill_between(line_plot['x'], ylim[0], line_plot['y'], color=line_plot['fill_colors'][1], alpha=0.2)

    # Setting the plot title and axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if show_legend and (X['label'] or (y and y['label'])):
        plt.legend()
    
    plt.show()

# Refactored functions
def plot_target_class_distribution(df, data_object):
    """
    Plot the distribution of target classes.

    Parameters:
    df (DataFrame): The dataset.
    data_object (Bunch): The data object containing target names.
    """
    plot_distribution(df, 'target', 'Distribution of Target Classes', 'Target', 'Count', data_object.target_names)

def plot_confusion_matrix(cm, data_object):
    """
    Plot the confusion matrix.

    Parameters:
    cm (array): The confusion matrix.
    data_object (Bunch): The data object containing target names.
    """
    plot_heatmap(cm, 'Confusion Matrix', 'Predicted', 'Actual', data_object.target_names, data_object.target_names)

def print_classification_report(y_test, y_pred, data_object):
    """
    Print the classification report.

    Parameters:
    y_test (array): The true labels.
    y_pred (array): The predicted labels.
    data_object (Bunch): The data object containing target names.
    """
    print_report(y_test, y_pred, data_object.target_names)

def scatter_plot_two_features(X_selected, feature1, feature2):
    """
    Create a scatter plot for two selected features.

    Parameters:
    X_selected (array): The selected features.
    feature1 (str): The name of the first feature.
    feature2 (str): The name of the second feature.
    """
    # Plot the graph
    scatter_plot(
        X={'data': [X_selected[:, 0], X_selected[:, 1]], 'color': 'blue', 'label': f'{feature1}'}, 
        title=f'{feature2} vs {feature1}', 
    )
    
def scatter_plot_with_class_labels(X, y, feature1, feature2):
    """
    Create a scatter plot with class labels.

    Parameters:
    X (array): The data.
    y (array): The labels.
    feature1 (str): The name of the first feature.
    feature2 (str): The name of the second feature.
    """

    breast_cancer = load_breast_cancer()

    feature1_index = np.argwhere(breast_cancer.feature_names == feature1).flatten()[0]
    feature2_index = np.argwhere(breast_cancer.feature_names == feature2).flatten()[0]

    # Defining benign data and malignant data
    benign_data = [X[y == 0][:, feature1_index], X[y == 0][:, feature2_index], "Benign"]
    malignant_data = [X[y == 1][:, feature1_index], X[y == 1][:, feature2_index], "Malignant"]

    # Plot the graph
    scatter_plot(
        X={'data': [benign_data[0], benign_data[1]], 'color': 'green', 'label': 'Benign'}, 
        y={'data': [malignant_data[0], malignant_data[1]], 'color': 'red', 'label': 'Malignant'}, 
        title=f'{feature2} vs {feature1}', 
        show_legend=True
    )

def scatter_plot_with_decision_boundary(X, y, model, feature1, feature2):
    """
    Create a scatter plot with a decision boundary.

    Parameters:
    X (array): The data.
    y (array): The labels.
    model (LogisticRegression): The logistic regression model.
    feature1 (str): The name of the first feature.
    feature2 (str): The name of the second feature.
    point_colors (list, optional): The colors for the data points of the classes.
    fill_colors (list, optional): The colors for the fill areas of the classes.
    """
    breast_cancer = load_breast_cancer()

    feature1_index = np.argwhere(breast_cancer.feature_names == feature1).flatten()[0]
    feature2_index = np.argwhere(breast_cancer.feature_names == feature2).flatten()[0]

    # Defining benign data and malignant data
    benign_data = [X[y == 0][:, feature1_index], X[y == 0][:, feature2_index], "Benign"]
    malignant_data = [X[y == 1][:, feature1_index], X[y == 1][:, feature2_index], "Malignant"]

    # Line Plot Coordinates
    x_values = np.linspace(X[:, feature1_index].min(), X[:, feature1_index].max(), 100)
    y_values = -(model.intercept_[0] + model.coef_[0][0] * x_values) / model.coef_[0][1]  # Decision boundary equation

    # Plot the graph
    scatter_plot(
        X={'data': [benign_data[0], benign_data[1]], 'color': 'green', 'label': 'Benign'}, 
        y={'data': [malignant_data[0], malignant_data[1]], 'color': 'red', 'label': 'Malignant'}, 
        line_plot={'x': x_values, 'y': y_values, 'color': 'blue', 'linestyle': '--'},
        title=f'{feature2} vs {feature1}', 
        show_legend=False
    )

def run_it_all_over():
    """
    Run the entire analysis: load data, select features, train model, and plot results.
    """
    # Load the dataset
    data = load_breast_cancer()
    X = data.data
    y = data.target

    # Randomly select two features to visualize
    feature_indices = random.sample(range(X.shape[1]), 2)
    feature1_index = feature_indices[0]
    feature2_index = feature_indices[1]

    # Extract the feature base names correctly
    feature1_base = data.feature_names[feature1_index].replace(' ', '_').lower()
    feature2_base = data.feature_names[feature2_index].replace(' ', '_').lower()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the logistic regression model
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train[:, feature_indices], y_train)  # Fit model only on selected features
    
    # Line Plot Coordinates
    x_values = np.linspace(X_test[:, feature1_index].min(), X_test[:, feature1_index].max(), 100)
    y_values = -(model.intercept_ + model.coef_[0][0] * x_values) / model.coef_[0][1]

    # Plot the graph
    scatter_plot(
        X={'data': [X_test[y_test == 0][:, feature1_index], X_test[y_test == 0][:, feature2_index]], 'color': 'green', 'label': data.target_names[0]}, 
        y={'data': [X_test[y_test == 1][:, feature1_index], X_test[y_test == 1][:, feature2_index]], 'color': 'red', 'label': data.target_names[1]},
        line_plot={'x': x_values, 'y': y_values, 'color': 'blue', 'linestyle': '--'},
        title=f'{data.feature_names[feature2_index]} vs {data.feature_names[feature1_index]}', 
        show_legend=True,
        xlabel=data.feature_names[feature1_index],
        ylabel=data.feature_names[feature2_index]
    )

    # Dictionary mapping feature names to their descriptions
    feature_descriptions = {
        'mean_radius': "Average distance from the center to the outer edge of the tumor.",
        'mean_texture': "How rough or smooth the surface of the tumor feels, on average.",
        'mean_perimeter': "The average length of the outline of the tumor.",
        'mean_area': "The average size of the surface of the tumor measured in square units.",
        'mean_smoothness': "How smooth or bumpy the tumor surface feels, averaged over several observations.",
        'mean_compactness': "A measure of how tightly the tumor cells are packed together, averaged over several observations.",
        'mean_concavity': "Average number of indentations or hollow areas on the tumor's surface.",
        'mean_concave_points': "Average number of sharp dips or points found along the contour of the tumor.",
        'mean_symmetry': "How evenly shaped the tumor is. A perfectly symmetrical tumor looks the same on both sides.",
        'mean_fractal_dimension': "A measure that describes the complexity of the tumor shape, showing how jagged the border is on average.",
        'radius_error': "The change in the tumor's radius across different measurements, indicating how much the size of the tumor varies.",
        'texture_error': "The change in the tumor's texture across different measurements, showing how much the roughness or smoothness varies.",
        'perimeter_error': "The change in the outline length of the tumor across different measurements, showing how much the outline varies.",
        'area_error': "The change in the surface size of the tumor across different measurements, showing how much the area varies.",
        'smoothness_error': "The change in how smooth or bumpy the tumor surface feels across different measurements.",
        'compactness_error': "The change in how tightly the tumor cells are packed together across different measurements.",
        'concavity_error': "The change in the number of indentations or hollow areas on the tumor's surface across different measurements.",
        'concave_points_error': "The change in the number of sharp dips or points found along the contour of the tumor across different measurements.",
        'symmetry_error': "The change in how evenly shaped the tumor is across different measurements.",
        'fractal_dimension_error': "The change in the complexity of the tumor shape across different measurements, showing how much the jaggedness of the border varies.",
        'worst_radius': "The largest distance from the center to the outer edge of the tumor observed among all measurements.",
        'worst_texture': "The roughest texture observed on the surface of the tumor.",
        'worst_perimeter': "The longest outline of the tumor measured among all observations.",
        'worst_area': "The largest surface area of the tumor measured among all observations.",
        'worst_smoothness': "The least smooth texture observed on the tumor's surface, indicating the roughest feel.",
        'worst_compactness': "The highest degree of how tightly the tumor cells are packed together, observed among all measurements.",
        'worst_concavity': "The deepest indentations observed on the tumor's surface.",
        'worst_concave_points': "The highest number of sharp dips or points observed along the contour of the tumor.",
        'worst_symmetry': "The most uneven shape observed in the tumor, where one side differs the most from the other.",
        'worst_fractal_dimension': "The highest complexity of the tumor shape observed, showing the most jagged border among all measurements."
    }
    
    # Print statements to describe the plotted graph and its components
    print(f"The graph plots \"{data.feature_names[feature1_index]}\" on the x-axis and \"{data.feature_names[feature2_index]}\" on the y-axis.\n"
        f"\t\"{data.feature_names[feature1_index]}\": {feature_descriptions[feature1_base]} (x-axis)\n"
        f"\t\"{data.feature_names[feature2_index]}\": {feature_descriptions[feature2_base]} (y-axis).\n\n"
        "The yellow points 🟢 represent \"benign tumors\", and the purple points 🔴 represent \"malignant tumors\".\n"
        "The red dashed line represents the decision boundary determined by the logistic regression model.\n\n" # explain what a decision boundary is better
        "Each run of this script might result in different features being selected, hence different visualizations and boundaries.\n")
    
    # Predict on the test set using the same features
    y_pred = model.predict(X_test[:, feature_indices])

    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy on test set:", accuracy)

def help_me_in_real_life():
    """
    Load the breast cancer dataset, train a logistic regression model, and visualize the results.

    This function performs the following steps:
    1. Loads the breast cancer dataset.
    2. Randomly selects two features for visualization.
    3. Splits the data into training and testing sets.
    4. Trains a logistic regression model using the selected features.
    5. Predicts the outcomes on the test set.
    6. Calculates and prints the accuracy of the model.
    7. Plots the decision boundary along with the data points, adjusting the y-axis limits.
    8. Fills the areas above and below the decision boundary to indicate the model's predictions.

    The visualization helps to understand the model's decision boundary and how well it separates the two classes.
    """
    # Load the dataset
    data = load_breast_cancer()
    X = data.data
    y = data.target

    # Randomly select two features to visualize
    feature_indices = random.sample(range(X.shape[1]), 2)
    feature1_index = feature_indices[0]
    feature2_index = feature_indices[1]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the logistic regression model
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train[:, feature_indices], y_train)  # Fit model only on selected features

    # Predict on the test set using the same features
    y_pred = model.predict(X_test[:, feature_indices])

    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    
    # Line Plot Coordinates
    x_values = np.linspace(X_test[:, feature1_index].min(), X_test[:, feature1_index].max(), 100)
    y_values = -(model.intercept_ + model.coef_[0][0] * x_values) / model.coef_[0][1]
    
    # Defining benign data and malignant data
    benign_data = [X_test[y_test == 0][:, feature1_index], X_test[y_test == 0][:, feature2_index], data.target_names[0]]
    malignant_data = [X_test[y_test == 1][:, feature1_index], X_test[y_test == 1][:, feature2_index], data.target_names[1]]

    # Plotting the data points and the decision boundary using scatter_plot
    scatter_plot(
        X={'data': [benign_data[0], benign_data[1]], 'color': 'blue', 'label': data.target_names[0]}, 
        y={'data': [malignant_data[0], malignant_data[1]], 'color': 'blue', 'label': data.target_names[1]}, 
        line_plot={'x': x_values, 'y': y_values, 'color': 'blue', 'linestyle': '--', 'fill_colors': ['green', 'red'], 'model': model},
        title=f'{data.feature_names[feature2_index]} vs {data.feature_names[feature1_index]}', 
        show_legend=False,
        xlabel=data.feature_names[feature1_index],
        ylabel=data.feature_names[feature2_index]
    )