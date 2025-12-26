import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, KNNImputer, IterativeImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy.stats import pearsonr
from imblearn.over_sampling import SMOTE


class MissingDataProcessor:
    def __init__(self, filepath):
        self.original_df = pd.read_csv(filepath)
        self.student_id = self.original_df['Student_ID']
        self.target = self.original_df['Stress_Level'].to_frame()
        self.data = self.original_df.drop(["Student_ID", "Stress_Level"], axis='columns')
        
        self.output_dir = "completed_data"
        os.makedirs(self.output_dir, exist_ok=True)

    def label_encode_categorical(self, data):
        categorical_columns = data.select_dtypes(exclude=['number']).columns
        le = LabelEncoder()
        for col in categorical_columns:
            data[col] = le.fit_transform(data[col].astype(str))
        return data

    def add_missing_data(self, data, missing_percentage, seed=None):
        if seed is not None:
            np.random.seed(seed)
        
        data_copy = data.copy()
        for column in data_copy.columns:
            col_missing_percentage = missing_percentage * np.random.uniform(0.5, 1.5)
            missing_mask = np.random.rand(len(data_copy)) < col_missing_percentage
            data_copy.loc[missing_mask, column] = np.nan
        
        return data_copy

    def fill_missing_data(self, data, method, random_seed=None):
        if random_seed is None:
            random_seed = np.random.randint(0, 2**32 - 1)
        else:
            random_seed = abs(random_seed) % (2**32)
        
        imputer_map = {
            'mean': SimpleImputer(strategy='mean'),
            'mode': SimpleImputer(strategy='most_frequent'),
            'knn': KNNImputer(n_neighbors=5),
            'multiple_imputation': IterativeImputer(max_iter=10, random_state=random_seed)
        }
        
        imputer = imputer_map.get(method)
        if imputer is None:
            raise ValueError(f"Unsupported imputation method: {method}")
        
        return pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

    def evaluate_imputation_methods(self, original_data, imputed_data):
        metrics = {}
        for column in original_data.columns:
            mask = original_data[column].isnull()
            
            if mask.sum() > 0:
                original_subset = original_data.loc[mask, column].dropna()
                imputed_subset = imputed_data.loc[mask, column][original_subset.index]
                
                if len(original_subset) > 0:
                    metrics[column] = {
                        'MAE': mean_absolute_error(original_subset, imputed_subset),
                        'MSE': mean_squared_error(original_subset, imputed_subset),
                        'Correlation': pearsonr(original_subset, imputed_subset)[0] 
                            if len(original_subset) > 1 else np.nan
                    }
                else:
                    metrics[column] = {
                        'MAE': np.nan,
                        'MSE': np.nan,
                        'Correlation': np.nan
                    }
        
        return metrics

    def balance_data_with_smote(self, data, target_column, random_seed=None):
        if random_seed is not None:
            np.random.seed(random_seed)
        
        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        smote = SMOTE(random_state=random_seed)
        X_balanced, y_balanced = smote.fit_resample(X, y)
        
        balanced_data = pd.concat([pd.DataFrame(X_balanced, columns=X.columns), 
                                   pd.DataFrame(y_balanced, columns=[target_column])], axis=1)
        
        return balanced_data

    def process_and_impute_with_smote(self, missing_percentages, methods):
        data_encoded = self.label_encode_categorical(self.data)
        
        le = LabelEncoder()
        target_encoded = self.target.copy()
        target_encoded['Stress_Level'] = le.fit_transform(target_encoded['Stress_Level'])
        
        all_method_metrics = {}
        
        for missing_percentage in missing_percentages:
            print(f"\nMissing data rate: {missing_percentage * 100}%")
            
            data_with_missing = self.add_missing_data(data_encoded, missing_percentage)
            
            method_results = {}
            
            for method in methods:
                print(f"\nMethod: {method}")
                
                completed_data = self.fill_missing_data(data_with_missing, method, random_seed=hash(method))
                
                completed_full_data = pd.concat([completed_data, target_encoded], axis=1)
                
                balanced_data = self.balance_data_with_smote(completed_full_data, target_column='Stress_Level')
                
                imputation_metrics = self.evaluate_imputation_methods(data_with_missing, completed_data)
                method_results[method] = imputation_metrics
                
                filename = os.path.join(
                    self.output_dir, 
                    f"student_{int(missing_percentage * 100)}_{method}.csv"
                )
                balanced_data.to_csv(filename, index=False)
                print(f"Balanced data saved: {filename}")
            
            all_method_metrics[missing_percentage] = method_results
        
        for missing_percentage, method_results in all_method_metrics.items():
            print(f"\nPerformance Results for {missing_percentage * 100}% Missing Data:")
            for method, metrics in method_results.items():
                print(f"\n{method.upper()} Method Metrics:")
                for column, metric_values in metrics.items():
                    print(f"  {column}:")
                    for metric_name, value in metric_values.items():
                        print(f"    {metric_name}: {value}")
processor = MissingDataProcessor('missing_data_files/student_lifestyle_dataset.csv')
processor.process_and_impute_with_smote(
    missing_percentages=[0.2, 0.4, 0.6], 
    methods=['mean', 'mode', 'knn', 'multiple_imputation']
)
