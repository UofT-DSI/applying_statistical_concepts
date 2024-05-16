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
    temperatures = np.random.uniform(60, 100, 500)  # Temperatures between 60 and 100 degrees
    ice_cream_sales = temperatures * 1.5 + np.random.normal(0, 10, 500)  # Sales with some noise

    # Reshape the data for sklearn
    X = temperatures.reshape(-1, 1)
    y = ice_cream_sales

    # Create a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)

    # Plot the data and the regression line
    plt.scatter(temperatures, ice_cream_sales, color='blue', label='Actual Sales')
    plt.plot(temperatures, predictions, color='red', label='Regression Line')
    plt.xlabel('Temperature (°F)')
    plt.ylabel('Ice Cream Sales')
    plt.title('Temperature vs Ice Cream Sales')
    plt.legend()
    plt.show()


def sleep_and_study():
    """
    Generate and plot a logistic regression model for hours studied and hours slept vs pass/fail outcome.
    """
    # Generate sample data: Hours studied, hours of sleep, and pass/fail outcomes
    np.random.seed(42)
    hours_studied = np.random.uniform(1, 10, 500)
    hours_sleep = np.random.uniform(4, 10, 500)
    pass_fail = (hours_studied + hours_sleep > 12).astype(int)

    # Fit the logistic regression model
    X = np.column_stack((hours_studied, hours_sleep))
    model = LogisticRegression()
    model.fit(X, pass_fail)

    # Generate a grid of values for prediction
    x_values = np.linspace(0, 12, 300)
    y_values = np.linspace(4, 10, 300)
    xx, yy = np.meshgrid(x_values, y_values)
    grid = np.c_[xx.ravel(), yy.ravel()]
    probs = model.predict_proba(grid)[:, 1].reshape(xx.shape)

    # Define custom colors for pass and fail
    custom_cmap = ListedColormap(['red', 'green'])

    # Plotting the data points and the decision boundary
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(hours_studied, hours_sleep, c=pass_fail, cmap=custom_cmap, edgecolor='k')
    plt.contour(xx, yy, probs, levels=[0.5], linestyles='dashed', colors='blue')
    plt.xlabel('Hours Studied')
    plt.ylabel('Hours of Sleep')
    plt.title('Logistic Regression: Decision Boundary with Two Features (100 Data Points)')

    # Adding a legend
    handles, labels = scatter.legend_elements()
    legend_labels = ['Fail', 'Pass']
    plt.legend(handles, legend_labels, title="Outcome")

    plt.show()

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

def scatter_plot(X, title, xlabel, ylabel, ylim):
    """
    Create a scatter plot.

    Parameters:
    X (array): The data to plot.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    ylim (tuple): The limits for the y-axis.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(*ylim)
    plt.show()

def scatter_plot_with_labels(X, y, title, xlabel, ylabel, ylim, colors):
    """
    Create a scatter plot with labels.

    Parameters:
    X (array): The data for the first class.
    y (array): The data for the second class.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    ylim (tuple): The limits for the y-axis.
    colors (list): The colors for the classes.
    """
    plt.figure(figsize=(8, 6))

    plt.scatter(X[0], X[1], color=colors[0], label=X[2], edgecolors='k')
    plt.scatter(y[0], y[1], color=colors[1], label=y[2], edgecolors='k')
        
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(*ylim)
    plt.legend()
    plt.show()

def scatter_plot_with_boundary(X, y, model_x, model_y, title, xlabel, ylabel, ylim, colors):
    """
    Create a scatter plot with a decision boundary.

    Parameters:
    X (array): The data for the first class.
    y (array): The data for the second class.
    model_x (array): The x-values for the decision boundary.
    model_y (array): The y-values for the decision boundary.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    ylim (tuple): The limits for the y-axis.
    colors (list): The colors for the classes.
    """
    plt.figure(figsize=(8, 6))

    plt.scatter(X[0], X[1], color=colors[0], label=X[2], edgecolors='k')
    plt.scatter(y[0], y[1], color=colors[1], label=y[2], edgecolors='k')

    plt.plot(model_x, model_y, color='blue', linestyle='--', label='Decision Boundary')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(*ylim)
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
    scatter_plot(X_selected, f'{feature2} vs {feature1}', feature1, feature2, (5, 45))

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

    benign_data = [X[y == 0][:, feature1_index], X[y == 0][:, feature2_index], "Benign"]
    malignant_data = [X[y == 1][:, feature1_index], X[y == 1][:, feature2_index], "Malignant"]

    scatter_plot_with_labels(benign_data, malignant_data, f'{feature2} vs {feature1}', feature1, feature2, 
                             (5, 45), ['green', 'red'])

def scatter_plot_with_decision_boundary(X, y, model, feature1, feature2):
    """
    Create a scatter plot with a decision boundary.

    Parameters:
    X (array): The data.
    y (array): The labels.
    model (LogisticRegression): The logistic regression model.
    feature1 (str): The name of the first feature.
    feature2 (str): The name of the second feature.
    """
    breast_cancer = load_breast_cancer()

    feature1_index = np.argwhere(breast_cancer.feature_names == feature1).flatten()[0]
    feature2_index = np.argwhere(breast_cancer.feature_names == feature2).flatten()[0]

    benign_data = [X[y == 0][:, feature1_index], X[y == 0][:, feature2_index], "Benign"]
    malignant_data = [X[y == 1][:, feature1_index], X[y == 1][:, feature2_index], "Malignant"]

    x_values = np.linspace(X[:, feature1_index].min(), X[:, feature1_index].max(), 100)
    y_values = -(model.intercept_ + model.coef_[0][0] * x_values) / model.coef_[0][1]  # Decision boundary equation

    scatter_plot_with_boundary(benign_data, malignant_data, x_values, y_values, f'{feature2} vs {feature1}', 
                               feature1, feature2, (5, 45), ['green', 'red'])
    

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

    # Plot the decision boundary and data points
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test[y_test == 0][:, feature1_index], X_test[y_test == 0][:, feature2_index], color='green', label=data.target_names[0], edgecolors='k')
    plt.scatter(X_test[y_test == 1][:, feature1_index], X_test[y_test == 1][:, feature2_index], color='red', label=data.target_names[1], edgecolors='k')
    
    x_values = np.linspace(X_test[:, feature1_index].min(), X_test[:, feature1_index].max(), 100)
    y_values = -(model.intercept_ + model.coef_[0][0] * x_values) / model.coef_[0][1]
    
    plt.plot(x_values, y_values, color='blue', linestyle='--', label='Decision Boundary')
    plt.title(f'{data.feature_names[feature2_index]} vs {data.feature_names[feature1_index]}')
    plt.xlabel(data.feature_names[feature1_index])
    plt.ylabel(data.feature_names[feature2_index])

    # Calculate y-axis limits with slight extension
    y_min = np.min(X_test[:, feature2_index])
    y_max = np.max(X_test[:, feature2_index])
    y_range = y_max - y_min
    y_extension = y_range * 0.1  # 10% extension

    plt.ylim(y_min - y_extension, y_max + y_extension)

    plt.legend()
    plt.show()

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

    # Plot the decision boundary and data points
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test[y_test == 0][:, feature1_index], X_test[y_test == 0][:, feature2_index], color='blue', label=data.target_names[0], edgecolors='k')
    plt.scatter(X_test[y_test == 1][:, feature1_index], X_test[y_test == 1][:, feature2_index], color='blue', label=data.target_names[1], edgecolors='k')
    
    x_values = np.linspace(X_test[:, feature1_index].min(), X_test[:, feature1_index].max(), 100)
    y_values = -(model.intercept_ + model.coef_[0][0] * x_values) / model.coef_[0][1]
    
    # Adjust y-axis limits to account for the decision boundary and fill areas
    y_min = X_test[:, feature2_index].min() - 1
    y_max = X_test[:, feature2_index].max() + 1
    plt.ylim(y_min, y_max)

    # Predict points above and below the decision boundary
    point_above = np.array([[x_values[0], y_values[0] + 1]])
    point_below = np.array([[x_values[0], y_values[0] - 1]])

    prediction_above = model.predict(point_above)

    if prediction_above == 1:
        plt.fill_between(x_values, y_values, y_max, color='red', alpha=0.2)
        plt.fill_between(x_values, y_min, y_values, color='green', alpha=0.2)
    else:
        plt.fill_between(x_values, y_values, y_max, color='green', alpha=0.2)
        plt.fill_between(x_values, y_min, y_values, color='red', alpha=0.2)

    plt.plot(x_values, y_values, color='blue', linestyle='--', label='Decision Boundary')
    plt.title(f'{data.feature_names[feature2_index]} vs {data.feature_names[feature1_index]}')
    plt.xlabel(data.feature_names[feature1_index])
    plt.ylabel(data.feature_names[feature2_index])
    
    plt.show()