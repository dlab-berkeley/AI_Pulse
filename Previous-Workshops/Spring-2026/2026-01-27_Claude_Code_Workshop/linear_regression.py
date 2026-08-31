"""
Linear Regression implementation using Ordinary Least Squares (OLS).

This module provides a LinearRegression class that implements OLS regression
from scratch using only numpy, scipy.stats, and matplotlib.
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


class LinearRegression:
    """
    Ordinary Least Squares (OLS) Linear Regression.

    Implements the closed-form solution: β = (X'X)^(-1)X'y

    Attributes
    ----------
    coefficients : ndarray
        Estimated coefficients for the regression (excluding intercept).
    intercept : float
        Estimated intercept (constant term).
    r_squared : float
        Coefficient of determination (R²).
    adj_r_squared : float
        Adjusted R² accounting for number of predictors.
    standard_errors : ndarray
        Standard errors of the coefficient estimates.

    Examples
    --------
    >>> X = np.array([[1], [2], [3], [4], [5]])
    >>> y = np.array([2.1, 4.0, 5.9, 8.1, 9.8])
    >>> model = LinearRegression()
    >>> model.fit(X, y)
    >>> model.predict([[6]])
    array([11.88])
    """

    def __init__(self):
        """Initialize the LinearRegression model."""
        self._coefficients = None
        self._intercept = None
        self._r_squared = None
        self._adj_r_squared = None
        self._standard_errors = None
        self._t_statistics = None
        self._p_values = None
        self._residuals = None
        self._fitted_values = None
        self._n_samples = None
        self._n_features = None
        self._feature_names = None
        self._mse = None
        self._X_with_intercept = None

    def fit(self, X, y, feature_names=None):
        """
        Fit the linear regression model using OLS closed-form solution.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data. Can be 1D array for simple regression.
        y : array-like of shape (n_samples,)
            Target values.
        feature_names : list of str, optional
            Names for each feature. If None, uses X1, X2, etc.

        Returns
        -------
        self : LinearRegression
            Fitted model.
        """
        X = np.asarray(X)
        y = np.asarray(y).flatten()

        # Handle 1D input
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        self._n_samples, self._n_features = X.shape

        # Set feature names
        if feature_names is not None:
            self._feature_names = list(feature_names)
        else:
            self._feature_names = [f'X{i+1}' for i in range(self._n_features)]

        # Add intercept column (column of ones)
        self._X_with_intercept = np.column_stack([np.ones(self._n_samples), X])

        # Closed-form OLS solution: β = (X'X)^(-1)X'y
        XtX = self._X_with_intercept.T @ self._X_with_intercept
        XtX_inv = np.linalg.inv(XtX)
        Xty = self._X_with_intercept.T @ y
        beta = XtX_inv @ Xty

        # Extract intercept and coefficients
        self._intercept = beta[0]
        self._coefficients = beta[1:]

        # Compute fitted values and residuals
        self._fitted_values = self._X_with_intercept @ beta
        self._residuals = y - self._fitted_values

        # Compute R² and adjusted R²
        ss_res = np.sum(self._residuals ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        self._r_squared = 1 - (ss_res / ss_tot)

        n, p = self._n_samples, self._n_features
        self._adj_r_squared = 1 - (1 - self._r_squared) * (n - 1) / (n - p - 1)

        # Compute standard errors
        dof = self._n_samples - self._n_features - 1  # degrees of freedom
        self._mse = ss_res / dof
        var_beta = self._mse * np.diag(XtX_inv)
        self._standard_errors = np.sqrt(var_beta)

        # Compute t-statistics and p-values
        self._t_statistics = beta / self._standard_errors
        self._p_values = 2 * (1 - stats.t.cdf(np.abs(self._t_statistics), dof))

        return self

    def predict(self, X):
        """
        Predict target values using the fitted model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Samples to predict.

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            Predicted values.

        Raises
        ------
        ValueError
            If the model has not been fitted.
        """
        if self._coefficients is None:
            raise ValueError("Model has not been fitted. Call fit() first.")

        X = np.asarray(X)
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        return self._intercept + X @ self._coefficients

    @property
    def coefficients(self):
        """ndarray: Estimated coefficients (excluding intercept)."""
        if self._coefficients is None:
            raise ValueError("Model has not been fitted. Call fit() first.")
        return self._coefficients.copy()

    @property
    def intercept(self):
        """float: Estimated intercept (constant term)."""
        if self._intercept is None:
            raise ValueError("Model has not been fitted. Call fit() first.")
        return self._intercept

    @property
    def r_squared(self):
        """float: Coefficient of determination (R²)."""
        if self._r_squared is None:
            raise ValueError("Model has not been fitted. Call fit() first.")
        return self._r_squared

    @property
    def adj_r_squared(self):
        """float: Adjusted R²."""
        if self._adj_r_squared is None:
            raise ValueError("Model has not been fitted. Call fit() first.")
        return self._adj_r_squared

    @property
    def standard_errors(self):
        """ndarray: Standard errors of coefficient estimates (including intercept)."""
        if self._standard_errors is None:
            raise ValueError("Model has not been fitted. Call fit() first.")
        return self._standard_errors.copy()

    @property
    def residuals(self):
        """ndarray: Residuals from the fitted model."""
        if self._residuals is None:
            raise ValueError("Model has not been fitted. Call fit() first.")
        return self._residuals.copy()

    def summary(self):
        """
        Print a formatted summary table of regression results.

        Similar to statsmodels OLS summary output, includes coefficients,
        standard errors, t-statistics, p-values, and model diagnostics.

        Returns
        -------
        str
            Formatted summary string.
        """
        if self._coefficients is None:
            raise ValueError("Model has not been fitted. Call fit() first.")

        # Build summary string
        width = 76
        lines = []
        lines.append("=" * width)
        lines.append("OLS Regression Results".center(width))
        lines.append("=" * width)

        # Model statistics
        lines.append(f"{'No. Observations:':<20} {self._n_samples:<15} "
                    f"{'R-squared:':<20} {self._r_squared:.6f}")
        lines.append(f"{'Df Residuals:':<20} {self._n_samples - self._n_features - 1:<15} "
                    f"{'Adj. R-squared:':<20} {self._adj_r_squared:.6f}")
        lines.append(f"{'Df Model:':<20} {self._n_features:<15} "
                    f"{'MSE:':<20} {self._mse:.6f}")
        lines.append("=" * width)

        # Coefficient table header
        lines.append(f"{'Variable':<15} {'Coefficient':>12} {'Std. Error':>12} "
                    f"{'t-statistic':>12} {'P>|t|':>12} {'':>10}")
        lines.append("-" * width)

        # Intercept row
        sig = self._get_significance_stars(self._p_values[0])
        lines.append(f"{'const':<15} {self._intercept:>12.6f} "
                    f"{self._standard_errors[0]:>12.6f} "
                    f"{self._t_statistics[0]:>12.4f} "
                    f"{self._p_values[0]:>12.4f} {sig:>10}")

        # Coefficient rows
        for i, name in enumerate(self._feature_names):
            sig = self._get_significance_stars(self._p_values[i + 1])
            lines.append(f"{name:<15} {self._coefficients[i]:>12.6f} "
                        f"{self._standard_errors[i + 1]:>12.6f} "
                        f"{self._t_statistics[i + 1]:>12.4f} "
                        f"{self._p_values[i + 1]:>12.4f} {sig:>10}")

        lines.append("-" * width)
        lines.append("Significance: *** p<0.001, ** p<0.01, * p<0.05, . p<0.1")
        lines.append("=" * width)

        summary_str = "\n".join(lines)
        print(summary_str)
        return summary_str

    def _get_significance_stars(self, p_value):
        """Return significance stars based on p-value."""
        if p_value < 0.001:
            return "***"
        elif p_value < 0.01:
            return "**"
        elif p_value < 0.05:
            return "*"
        elif p_value < 0.1:
            return "."
        return ""

    def plot_fit(self, X, y, feature_idx=0, ax=None, figsize=(10, 6)):
        """
        Plot the regression fit with observed data points.

        For multiple regression, plots the relationship between one feature
        and y, with other features held at their mean values.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Feature data.
        y : array-like of shape (n_samples,)
            Target values.
        feature_idx : int, default=0
            Index of feature to plot (for multiple regression).
        ax : matplotlib.axes.Axes, optional
            Axes object to plot on. If None, creates new figure.
        figsize : tuple, default=(10, 6)
            Figure size if creating new figure.

        Returns
        -------
        ax : matplotlib.axes.Axes
            The axes object containing the plot.
        """
        if self._coefficients is None:
            raise ValueError("Model has not been fitted. Call fit() first.")

        X = np.asarray(X)
        y = np.asarray(y).flatten()

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)

        # Get feature values for plotting
        x_plot = X[:, feature_idx]
        feature_name = self._feature_names[feature_idx]

        # Scatter plot of actual data
        ax.scatter(x_plot, y, alpha=0.6, edgecolors='black',
                   linewidth=0.5, label='Observed', color='steelblue')

        # Regression line
        x_range = np.linspace(x_plot.min(), x_plot.max(), 100)

        if self._n_features == 1:
            # Simple regression
            y_pred = self._intercept + self._coefficients[0] * x_range
        else:
            # Multiple regression: hold other features at their means
            X_pred = np.tile(X.mean(axis=0), (100, 1))
            X_pred[:, feature_idx] = x_range
            y_pred = self.predict(X_pred)

        ax.plot(x_range, y_pred, color='crimson', linewidth=2,
                label=f'Fitted (R² = {self._r_squared:.4f})')

        # Labels and formatting
        ax.set_xlabel(feature_name, fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.set_title(f'Linear Regression: {feature_name} vs y', fontsize=14)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        return ax


if __name__ == "__main__":
    # Example usage
    np.random.seed(42)

    # Generate sample data
    n = 100
    X = np.random.uniform(0, 10, (n, 2))
    y = 3 + 2 * X[:, 0] - 1.5 * X[:, 1] + np.random.normal(0, 1, n)

    # Fit model
    model = LinearRegression()
    model.fit(X, y, feature_names=['Feature_A', 'Feature_B'])

    # Print summary
    model.summary()

    # Make predictions
    X_new = np.array([[5, 3], [7, 2]])
    predictions = model.predict(X_new)
    print(f"\nPredictions for new data: {predictions}")

    # Plot fit
    model.plot_fit(X, y, feature_idx=0)
    plt.show()
