import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import klib as krishna
import numpy as np
import random
from matplotlib import *
from streamlit_option_menu import option_menu
import chardet




class Statistics:
    def __init__(self, dataset):
        self.dataset = dataset

    def basic_details(self):
        st.subheader("Basic Details")

        st.text(f"Number of Rows: {self.dataset.shape[0]}")
        st.text(f"Number of Columns: {self.dataset.shape[1]}")
        st.text(f"Number of Missing Values: {self.dataset.isnull().sum().sum()}")
        st.text(f"Size of the Dataset: {self.dataset.size}")
        st.text(f"Column Names: {self.dataset.columns.tolist()}")
        st.text(f"Index Names: {self.dataset.index.tolist()}")

        st.subheader("First 5 Rows:")
        st.dataframe(self.dataset.head())

        st.subheader("Last 10 Rows:")
        st.dataframe(self.dataset.tail(10))

        st.subheader("Random Sample (20% of Data):")
        st.dataframe(self.dataset.sample(frac=0.2))

    def secondary_information(self):
        st.subheader("Secondary Information")

        st.text("Column Data Types:")
        st.dataframe(self.dataset.dtypes)

        st.text("Memory Usage:")
        memory_usage_df = pd.DataFrame(self.dataset.memory_usage(deep=True), columns=['Memory Usage (bytes)'])
        st.dataframe(memory_usage_df)

        # Display numerical data types if they exist
        numerical_data = self.dataset.select_dtypes(include=['number','int32','int64','float32','float64'])
        if not numerical_data.empty:
            st.subheader("Numerical Data Columns:")
            st.dataframe(numerical_data)

        # Display categorical and time series data if they exist
        categorical_data = self.dataset.select_dtypes(include=['category', 'object','string'])
        time_series_data = self.dataset.select_dtypes(include=['datetime'])

        if not categorical_data.empty:
            st.subheader("Categorical Data Columns:")
            st.dataframe(categorical_data)
        
        if not time_series_data.empty:
            st.subheader("Time Series Data Columns:")
            st.dataframe(time_series_data)

    def statistics_1(self):
        st.subheader("Statistics - 1")

        # Display basic statistical summary
        st.text("Statistical Summary (describe):")
        st.dataframe(self.dataset.describe())

        # Display DataFrame information
        st.text("DataFrame Info:")
        st.write(self.dataset.info())
        
        
    def statistics_2(self):
        st.subheader("Statistics - 2")
        if True:
            st.text("Mean Values (by Columns):")
            mean_df = self.dataset.mean(numeric_only=True,skipna=True)  # Calculate mean across columns
            st.dataframe(mean_df)
            plt.figure(figsize=(10, 4))
            plt.bar(mean_df.index,mean_df.values)
            plt.plot(mean_df.index.tolist(),mean_df.values.tolist(),color="red",marker="o",mec="black",mfc="blue")
            plt.xticks(rotation=45, ha='right')
            plt.title("Mean Values (by Columns)")
            st.pyplot(plt)  # Display the figure

            st.text("Median Values (by Columns):")
            median_df = self.dataset.median(numeric_only=True,skipna=True)  # Calculate median across columns
            st.dataframe(median_df)
            plt.figure(figsize=(10, 4))
            plt.bar(mean_df.index,mean_df.values)
            plt.plot(mean_df.index.tolist(),mean_df.values.tolist(),color="red",marker="o",mec="black",mfc="blue")
            plt.xticks(rotation=45, ha='right')
            plt.title("Median Values (by Columns)")
            st.pyplot(plt.gcf())

            st.text("Mode Values (by Columns):")
            mode_df = self.dataset.mode(numeric_only=False)  # Calculate mode across columns
            st.dataframe(mode_df)
            plt.figure(figsize=(10, 4))
            sns.countplot(x=mode_df.index)
            plt.xticks(rotation=45, ha='right')
            plt.title("Mode Values (by Columns)")
            st.pyplot(plt.gcf())

            st.text("Correlation Matrix (by Columns):")
            corr_df = self.dataset.corr(numeric_only=True)  # Calculate correlation matrix across columns
            st.dataframe(corr_df)
            plt.figure(figsize=(10, 4))
            sns.heatmap(corr_df, annot=True, fmt='.2f', cmap='coolwarm')
            plt.title("Correlation Matrix (by Columns)")
            st.pyplot(plt.gcf())

            st.text("Covariance Matrix (by Columns):")
            cov_df = self.dataset.cov(numeric_only=True)  # Calculate covariance matrix across columns
            st.dataframe(cov_df)
            plt.figure(figsize=(10, 4))
            sns.heatmap(cov_df, annot=True, fmt='.2f', cmap='coolwarm')
            plt.title("Covariance Matrix (by Columns)")
            st.pyplot(plt.gcf())

            st.text("Variance (by Columns):")
            var_df = self.dataset.var(numeric_only=True,skipna=True)  # Calculate variance across columns
            st.dataframe(var_df)
            plt.figure(figsize=(10, 4))
            plt.bar(var_df.index, var_df.values)
            plt.plot(mean_df.index.tolist(),mean_df.values.tolist(),color="red",marker="o",mec="black",mfc="blue")
            plt.xticks(rotation=45, ha='right')
            plt.title("Variance (by Columns)")
            st.pyplot(plt)

            st.text("Standard Deviation (by Columns):")
            std_df = self.dataset.std(numeric_only=True,skipna=True)  # Calculate standard deviation across columns
            st.dataframe(std_df)
            plt.figure(figsize=(10, 4))
            plt.bar(std_df.index, std_df.values)
            plt.plot(std_df.index.tolist(),mean_df.values.tolist(),color="red",marker="o",mec="black",mfc="blue")
            plt.xticks(rotation=45, ha='right')
            plt.title("Standard Deviation (by Columns)")
            st.pyplot(plt)

            st.text("Standard Error of Mean (by Columns):")
            sem_df = self.dataset.sem(numeric_only=True,skipna=True)  # Calculate SEM across columns
            st.dataframe(sem_df)
            plt.figure(figsize=(10, 4))
            plt.bar(sem_df.index, sem_df.values)
            plt.plot(list(sem_df.index), sem_df.values.tolist(),color="red",marker="o",mec="black",mfc="blue")
            plt.xticks(rotation=45, ha='right')
            plt.title("Standard Error of Mean (by Columns)")
            st.pyplot(plt.gcf())

            st.text("Skewness (by Columns):")
            skew_df = self.dataset.skew(numeric_only=True,skipna=True)  # Calculate skewness across columns
            st.dataframe(skew_df)
            plt.figure(figsize=(10, 4))
            plt.bar(skew_df.index, skew_df.values)
            plt.plot(skew_df.index.tolist(), skew_df.values.tolist(),color="red",marker="o",mec="black",mfc="blue")
            plt.xticks(rotation=45, ha='right')
            plt.title("Skewness (by Columns)")
            st.pyplot(plt.gcf())

            st.text("Kurtosis (by Columns):")
            kurt_df = self.dataset.kurt(numeric_only=True,skipna=True)  # Calculate kurtosis across columns
            st.dataframe(kurt_df)
            plt.figure(figsize=(10, 4))
            plt.bar(kurt_df.index, kurt_df.values)
            plt.plot(skew_df.index.tolist(), skew_df.values.tolist(),color="red",marker="o",mec="black",mfc="blue")
            plt.xticks(rotation=45, ha='right')
            plt.title("Kurtosis (by Columns)")
            st.pyplot(plt.gcf())

        

class Krishna:
    def __init__(self,dataset):
        self.dataset=dataset
    def main(self):
        krishna.missing_plot(dataset)


        
class UnivariateWithoutHue:
     def __init__(self, dataset):
        self.dataset = dataset
        self.numeric_data_types = ["int8", "int16", "int32", "int64", "uint8", "uint16", "uint32", "uint64", "float16", "float32", "float64"]
        self.categorical_data_types = ["category", "object", "string", "datetime64[ns]", "bool"]
     def extract_columns(self):
        cc = self.dataset.select_dtypes(include=self.categorical_data_types, exclude=self.numeric_data_types).columns
        nc = self.dataset.select_dtypes(include=self.numeric_data_types, exclude=self.categorical_data_types).columns
        return cc, nc

     def plot_histplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.histplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_kdeplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.kdeplot(data=self.dataset[col], fill=True)
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_boxplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.boxplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_violinplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.violinplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_stripplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.stripplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_swarmplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.swarmplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_ecdfplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.ecdfplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_rugplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.rugplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def plot_lineplot(self, numerical_columns):
        plt.figure(figsize=(15, 5))
        for count, col in enumerate(numerical_columns, start=1):
            plt.subplot(1, len(numerical_columns), count)
            plt.title(f"Univariate Analysis with {col}")
            sns.lineplot(data=self.dataset[col])
            plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

     def layout(self, nc):
        plot_dict = {
            'histplot': self.plot_histplot,
            'kdeplot': self.plot_kdeplot,
            'boxplot': self.plot_boxplot,
            'violinplot': self.plot_violinplot,
            'stripplot': self.plot_stripplot,
            'swarmplot': self.plot_swarmplot,
            'ecdfplot': self.plot_ecdfplot,
            'rugplot': self.plot_rugplot,
            'lineplot': self.plot_lineplot
        }
        
        if st.checkbox("Histplot With Out Hue"):
            plot_dict['histplot'](nc)
        if st.checkbox("KDE Plot With Out Hue"):
            plot_dict['kdeplot'](nc)
        if st.checkbox("Box Plot With Out Hue"):
            plot_dict['boxplot'](nc)
        if st.checkbox("Violin Plot With Out Hue"):
            plot_dict['violinplot'](nc)
        if st.checkbox("Strip Plot With Out Hue"):
            plot_dict['stripplot'](nc)
        if st.checkbox("Swarm Plot With Out Hue"):
            plot_dict['swarmplot'](nc)
        if st.checkbox("ECDF Plot With Out Hue"):
            plot_dict['ecdfplot'](nc)
        if st.checkbox("RUG Plot With Out Hue"):
            plot_dict['rugplot'](nc)
        if st.checkbox("Line Plot With Out Hue"):
            plot_dict['lineplot'](nc)

class UnivariateAnalysisWithHue:
    def __init__(self, data):
        self.dataset = data
        self.numeric_data_types = ["int8", "int16", "int32", "int64", "uint8", "uint16", "uint32", "uint64", "float16", "float32", "float64"]
        self.categorical_data_types = ["category", "object", "string", "bool"]
        
        # Initialize plot dictionary
        self.plot_dict = {
            'histplot': self.plot_histplot,
            'kdeplot': self.plot_kdeplot,
            'boxplot': self.plot_boxplot,
            'violinplot': self.plot_violinplot,
            'stripplot': self.plot_stripplot,
            'swarmplot': self.plot_swarmplot,
            'ecdfplot': self.plot_ecdfplot,
            'rugplot': self.plot_rugplot,
            'lineplot': self.plot_lineplot
        }
        self.value=st.slider("Select the hue features that contain at most given unique features in a particuler feature",min_value=1,max_value=100)
        
        # Extract categorical and numerical columns
        self.cc = [x for x in self.dataset.select_dtypes(include=self.categorical_data_types, exclude=self.numeric_data_types).columns if self.dataset[x].nunique()<=self.value]
        self.cc1 = [x for x in self.dataset.select_dtypes(include=self.categorical_data_types, exclude=self.numeric_data_types).columns if self.dataset[x].nunique()>self.value]
        self.nc = self.dataset.select_dtypes(include=self.numeric_data_types, exclude=self.categorical_data_types).columns

    def plot_histplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.histplot(x=self.dataset[col],hue=self.dataset[hue])
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_kdeplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.kdeplot(x=self.dataset[col],hue=self.dataset[hue], fill=True)
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_boxplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.boxplot(x=self.dataset[col],hue=self.dataset[hue])
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_violinplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.violinplot(x=self.dataset[col],hue=self.dataset[hue])
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_stripplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.stripplot(data=self.dataset, x=col, hue=hue)
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_swarmplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.swarmplot(x=self.dataset[col],hue=self.dataset[hue])
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_ecdfplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.ecdfplot(x=self.dataset[col],hue=self.dataset[hue])
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_rugplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.rugplot(x=self.dataset[col],hue=self.dataset[hue])
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def plot_lineplot(self):
        plt.figure(figsize=(10, 25))
        cnt = 0
        for col in self.nc:
            for hue in self.cc:
                cnt += 1
                plt.subplot(len(self.nc), len(self.cc), cnt)
                sns.lineplot(x=self.dataset[col],hue=self.dataset[hue])
                plt.xlabel(col)
        plt.tight_layout()
        st.pyplot(plt)

    def layout(self):
        st.info(f"These values {self.cc1} have high cardinality, resulting in hundreds of plots, hence not included in plot generation")
        if st.checkbox("Histplot With Hue"):
            self.plot_dict['histplot']()
        if st.checkbox("KDE Plot With Hue"):
            self.plot_dict['kdeplot']()
        if st.checkbox("Box Plot With Hue"):
            self.plot_dict['boxplot']()
        if st.checkbox("Violin Plot With Hue"):
            self.plot_dict['violinplot']()
        if st.checkbox("Strip Plot With Hue"):
            self.plot_dict['stripplot']()
        if st.checkbox("Swarm Plot With Hue"):
            self.plot_dict['swarmplot']()
        if st.checkbox("ECDF Plot With Hue"):
            self.plot_dict['ecdfplot']()
        if st.checkbox("RUG Plot With Hue"):
            self.plot_dict['rugplot']()
        if st.checkbox("Line Plot With Hue"):
            self.plot_dict['lineplot']()

class Displot:
    def __init__(self,dataset):
        self.dataset=dataset
        self.columns=list(self.dataset.columns)
        self.x=st.selectbox("x for displot",[None]+self.columns)
        self.y=st.selectbox("y for displot",[None]+self.columns)
        self.hue=st.selectbox("hue for displot",[None]+self.columns)
        if self.hue:
            self.hue_order=st.multiselect("hue_order for displot",self.dataset[self.hue].unique())
            self.hue_norm=st.text_input("(Displot}Enter coma separeted ranges for hue norm")
        else:
            self.hue_order=None
            self.hue_norm=None
        self.col=st.selectbox("(Displot) col parameter",[None]+self.columns)
        if self.col:
            self.col_order_list=self.dataset[self.col].unique()
            self.col_order=st.multiselect("(Displot) col_order parameter",self.col_order_list)
            self.col_wrap=st.slider("(Displot) col_wrap parameter",min_value=1,max_value=100,value=3)
        else:
            self.col_order=None
            self.col_wrap=None
        self.row=st.selectbox("(Dis plot) row parameter",[None]+self.columns)
        if self.row:
            self.row_order_list=self.dataset[self.row].unique()
            self.row_order=st.multiselect("(displot) row_order parameter",self.row_order_list)
        else:
            self.row_order=None
        self.kind=st.selectbox("(Displot) kind parameter",["hist","kde","ecdf"])
        self.rug=st.checkbox(" (Displot) rug parameter ")
        self.legend=st.selectbox("(Displot) legend parameter",[True,False])
        self.palette = st.selectbox("(Displot) palette parameter", ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'bone', 'cool', 'copper', 'cubehelix', 'gnuplot', 'gnuplot2', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'twilight', 'winter', 'Spectral', 'coolwarm', 'bwr', 'seismic'])
        self.height=st.slider("(Displot) height parameter",min_value=1,max_value=100,value=4)
        self.aspect=st.slider("(Displot) aspect parameter",min_value=1,max_value=100,value=4)
    def plot(self):
        sns.displot(data=self.dataset,x=self.x,y=self.y,hue=self.hue,hue_order=self.hue_order,col=self.col,
                    col_order=self.col_order,col_wrap=self.col_wrap,row=self.row,
                    row_order=self.row_order,kind=self.kind,rug=self.rug,legend=self.legend,
                    palette=self.palette,height=self.height,aspect=self.aspect)
        st.pyplot(plt)


class Histplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        
        # Parameters with selectboxes and validation
        self.x = st.selectbox("(sns.histplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.histplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.histplot) hue", [None] + self.columns)
        if self.hue:
            self.hue_order = st.multiselect("(sns.histplot) hue_order", self.dataset[self.hue].unique())
            self.hue_norm = st.text_input("(sns.histplot) hue_norm")
        else:
            self.hue_order = None
            self.hue_norm = None
            
        self.stat = st.selectbox('(sns.histplot) stat parameter', ['count', 'frequency', 'percent', 'probability', 'density'])
        self.multiple = st.selectbox('(sns.histplot) multiple parameter', ['layer', 'dodge', 'stack', 'fill'])
        self.element = st.selectbox('(sns.histplot) element parameter', ['bars', 'step', 'poly'])
        self.kde = st.selectbox("(sns.histplot) kde parameter", self.bool)
        self.fill = st.selectbox("(sns.histplot) fill parameter", self.bool)
        self.shrink = st.slider("(sns.histplot) shrink parameter", min_value=0.1, max_value=1.0, value=1.0, step=0.1)
        
        # Threshold, pthresh, pmax conditionally based on kde
        if self.kde:
            self.pthresh = st.radio("(sns.histplot) pthresh parameter", ["None", "Specify"])
            self.pthresh = st.slider("Specify pthresh", 0.0, 1.0, 0.05) if self.pthresh == "Specify" else None
            
            self.pmax = st.radio("(sns.histplot) pmax parameter", ["None", "Specify"])
            self.pmax = st.slider("Specify pmax", 0.0, 1.0, 0.1) if self.pmax == "Specify" else None
        else:
            self.pthresh, self.pmax = None, None
        
        # Threshold and bin handling
        self.thresh = st.slider("(sns.histplot) thresh parameter", min_value=0.0, max_value=1.0, value=0.0)
        self.discrete = st.selectbox("(sns.histplot) discrete parameter", [None, True, False])
        
        if st.checkbox("Bins Area"):
            self.common_bins = st.selectbox("(sns.histplot) common_bins parameter", self.bool)
            self.bins = st.radio("(sns.histplot) bins parameter", ["None", "Specify", "Auto"])
            if self.bins == "Specify":
                self.bins = st.slider("Number of bins", min_value=1, max_value=100, value=5)
            else:
                self.bins = 'auto'
            
            self.binwidth = st.radio("(sns.histplot) binwidth parameter", ["None", "Specify"])
            self.binwidth = st.slider("Specify binwidth", min_value=0.1, max_value=10.0, value=1.0) if self.binwidth == "Specify" else None
            
            self.binrange = st.radio("(sns.histplot) binrange parameter", ["None", "Specify"])
            if self.binrange == "Specify":
                bin_start = st.slider("Start of bin range", min_value=float(self.dataset[self.x].min()), max_value=float(self.dataset[self.x].max()), value=float(self.dataset[self.x].min()))
                bin_end = st.slider("End of bin range", min_value=float(self.dataset[self.x].min()), max_value=float(self.dataset[self.x].max()), value=float(self.dataset[self.x].max()))
                self.binrange = (bin_start, bin_end)
            else:
                self.binrange = None
        else:
            self.bins, self.binwidth, self.binrange, self.common_bins = 'auto', None, None, True
        
        # Other optional parameters
        self.cbar = st.selectbox("(sns.histplot) cbar parameter", self.bool)
        self.legend = st.selectbox("(sns.histplot) legend parameter", self.bool)
        self.cumulative = st.selectbox("(sns.histplot) cumulative parameter", self.bool)
        self.common_norm = st.selectbox("(sns.histplot) common_norm parameter", self.bool)
        self.palette = st.selectbox("(sns.histplot) palette parameter", ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'bone', 'cool', 'copper', 'cubehelix', 'gnuplot', 'gnuplot2', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'twilight', 'winter', 'Spectral', 'coolwarm', 'bwr', 'seismic'])

    def plot(self):
        sns.histplot(data=self.dataset,
                     x=self.x, y=self.y, hue=self.hue,
                     stat=self.stat, bins=self.bins, binwidth=self.binwidth,
                     binrange=self.binrange, discrete=self.discrete, cumulative=self.cumulative,
                     common_bins=self.common_bins, common_norm=self.common_norm, multiple=self.multiple,
                     element=self.element, fill=self.fill, shrink=self.shrink, kde=self.kde,
                     thresh=self.thresh, pthresh=self.pthresh, pmax=self.pmax, cbar=self.cbar,
                     palette=self.palette, hue_order=self.hue_order, hue_norm=self.hue_norm,
                     legend=self.legend)
        st.pyplot(plt)

class Kdeplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        self.x = st.selectbox("(sns.kdeplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.kdeplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.kdeplot) hue", [None] + self.columns)        
        if self.hue:
            self.hue_order = st.multiselect("(sns.kdeplot) hue_order", self.dataset[self.hue].unique())
            self.hue_norm = st.text_input("(sns.kdeplot) hue_norm")
        else:
            self.hue_order = None
            self.hue_norm = None        
        self.palette = st.selectbox("(sns.kdeplot) palette parameter", ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'bone', 'cool', 'copper', 'cubehelix', 'gnuplot', 'gnuplot2', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'twilight', 'winter', 'Spectral', 'coolwarm', 'bwr', 'seismic'])
        self.fill = st.selectbox("(sns.kdeplot) fill parameter", self.bool)
        self.multiple = st.selectbox("(sns.kdeplot) multiple parameter", ['layer', 'stack', 'fill','dodge'])
        self.common_norm = st.selectbox("(sns.kdeplot) common_norm parameter", self.bool)
        self.common_grid = st.selectbox("(sns.kdeplot) common_grid parameter", self.bool)
        self.cumulative = st.selectbox("(sns.kdeplot) cumulative parameter", self.bool)
        self.bw_method = st.selectbox("(sns.kdeplot) bw_method parameter", ['scott', 'silverman', 'Custom'])
        self.bw_adjust = st.slider("(sns.kdeplot) bw_adjust parameter", min_value=0.1, max_value=2.0, value=1.0, step=0.1)        
        if self.bw_method == 'Custom':
            self.bw_method = st.text_input("Custom bw_method", value="")        
        self.log_scale = st.radio("(sns.kdeplot) log_scale parameter", [None, "x", "y", "both"])
        self.levels = st.slider("(sns.kdeplot) levels parameter", min_value=1, max_value=100, value=10)
        self.thresh = st.slider("(sns.kdeplot) thresh parameter", min_value=0.0, max_value=1.0, value=0.05)
        self.gridsize = st.slider("(sns.kdeplot) gridsize parameter", min_value=50, max_value=500, value=200)
        self.cut = st.slider("(sns.kdeplot) cut parameter", min_value=0.0, max_value=5.0, value=3.0, step=0.1)        
        self.clip = st.radio("(sns.kdeplot) clip parameter", [None, "Specify"])
        if self.clip == "Specify":
            clip_min = st.number_input("Clip Min", value=float(self.dataset[self.x].min()))
            clip_max = st.number_input("Clip Max", value=float(self.dataset[self.x].max()))
            self.clip = (clip_min, clip_max)
        else:
            self.clip = None        
        self.cbar = st.selectbox("(sns.kdeplot) cbar parameter", self.bool)
        self.legend = st.selectbox("(sns.kdeplot) legend parameter", self.bool)
    
    def plot(self):
        sns.kdeplot(data=self.dataset,
                    x=self.x, y=self.y, hue=self.hue,
                    palette=self.palette, fill=self.fill, multiple=self.multiple,
                    common_norm=self.common_norm, common_grid=self.common_grid,
                    cumulative=self.cumulative, bw_method=self.bw_method,
                    bw_adjust=self.bw_adjust, log_scale=self.log_scale,
                    levels=self.levels, thresh=self.thresh, gridsize=self.gridsize,
                    cut=self.cut, clip=self.clip, cbar=self.cbar, hue_order=self.hue_order,
                    hue_norm=self.hue_norm, legend=self.legend)
        st.pyplot(plt)


class Ecdfplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        
        # Parameters with selectboxes and validation
        self.x = st.selectbox("(sns.ecdfplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.ecdfplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.ecdfplot) hue", [None] + self.columns)
        
        if self.hue:
            self.hue_order = st.multiselect("(sns.ecdfplot) hue_order", self.dataset[self.hue].unique())
            self.hue_norm = st.text_input("(sns.ecdfplot) hue_norm")
        else:
            self.hue_order = None
            self.hue_norm = None
            
        self.stat = st.selectbox("(sns.ecdfplot) stat parameter", ['proportion', 'count', 'density'])
        self.complementary = st.selectbox("(sns.ecdfplot) complementary parameter", self.bool)
        self.log_scale = st.radio("(sns.ecdfplot) log_scale parameter", [None, "x", "y", "both"])
        
        self.palette = st.selectbox("(sns.ecdfplot) palette parameter", ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'bone', 'cool', 'copper', 'cubehelix', 'gnuplot', 'gnuplot2', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'twilight', 'winter', 'Spectral', 'coolwarm', 'bwr', 'seismic'])
        self.legend = st.selectbox("(sns.ecdfplot) legend parameter", self.bool)
        
    def plot(self):
        sns.ecdfplot(data=self.dataset,
                     x=self.x, y=self.y, hue=self.hue, stat=self.stat,
                     complementary=self.complementary, palette=self.palette,
                     hue_order=self.hue_order, hue_norm=self.hue_norm,
                     log_scale=self.log_scale, legend=self.legend)
        st.pyplot(plt)



class Rugplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        self.x = st.selectbox("(sns.rugplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.rugplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.rugplot) hue", [None] + self.columns)

        if self.hue:
            self.hue_order = st.multiselect("(sns.rugplot) hue_order", self.dataset[self.hue].unique())
            self.hue_norm = st.text_input("(sns.rugplot) hue_norm")
        else:
            self.hue_order = None
            self.hue_norm = None

        self.height = st.slider("(sns.rugplot) height parameter", min_value=0.01, max_value=0.1, value=0.025, step=0.005)
        self.expand_margins = st.selectbox("(sns.rugplot) expand_margins parameter", self.bool)
        self.palette = st.selectbox("(sns.rugplot) palette parameter", ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'bone', 'cool', 'copper', 'cubehelix', 'gnuplot', 'gnuplot2', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'twilight', 'winter', 'Spectral', 'coolwarm', 'bwr', 'seismic'])
        self.legend = st.selectbox("(sns.rugplot) legend parameter", self.bool)

    def plot(self):
        sns.rugplot(data=self.dataset,
                    x=self.x, y=self.y, hue=self.hue, height=self.height,
                    expand_margins=self.expand_margins, palette=self.palette,
                    hue_order=self.hue_order, hue_norm=self.hue_norm,
                    legend=self.legend)
        st.pyplot(plt)



class Catplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        self.x = st.selectbox("(sns.catplot) x", [None] + self.columns)
        self.order = st.multiselect("(sns.catplot) order", self.dataset[self.x].unique()) if self.x else None
        self.y = st.selectbox("(sns.catplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.catplot) hue", [None] + self.columns)
        self.row = st.selectbox("(sns.catplot) row", [None] + self.columns)
        self.col = st.selectbox("(sns.catplot) col", [None] + self.columns)
        self.row_order = st.multiselect("(sns.catplot) row_order", self.dataset[self.row].unique()) if self.row else None
        self.col_order = st.multiselect("(sns.catplot) col_order", self.dataset[self.col].unique()) if self.col else None
        self.col_wrap = st.slider("(sns.catplot) col_wrap", min_value=1, max_value=10, value=4) if self.col else None
        self.units = st.selectbox("(sns.catplot) units", [None] + self.columns)
        self.weights = st.selectbox("(sns.catplot) weights", [None] + self.columns)
        self.kind = st.selectbox("(sns.catplot) kind", ['strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count'])
        self.estimator = st.selectbox("(sns.catplot) estimator", [None, 'mean', 'median', 'sum', 'std', 'var', 'min', 'max'])   
        self.errorbar = st.selectbox("(sns.catplot) errorbar", ['ci', 'pi', 'se', 'sd', 'range', 'percentile', 'var'], index=0)
        self.n_boot = st.slider("(sns.catplot) n_boot", min_value=100, max_value=5000, value=1000, step=100)
        self.hue_order = st.multiselect("(sns.catplot) hue_order", self.dataset[self.hue].unique()) if self.hue else None
        self.log_scale = st.selectbox("(sns.catplot) log_scale", [None, True, False])
        self.palette = st.selectbox("(sns.catplot) palette", ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'bone', 'cool', 'copper', 'cubehelix', 'gnuplot', 'gnuplot2', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'twilight', 'winter', 'Spectral', 'coolwarm', 'bwr', 'seismic']) 
        self.legend = st.selectbox("(sns.catplot) legend", ['auto', True, False])
        self.legend_out = st.selectbox("(sns.catplot) legend_out", self.bool)
        self.sharex = st.selectbox("(sns.catplot) sharex", self.bool)
        self.sharey = st.selectbox("(sns.catplot) sharey", self.bool)
        self.margin_titles = st.selectbox("(sns.catplot) margin_titles", self.bool)

    def plot(self):
        sns.catplot(data=self.dataset,
                    x=self.x, y=self.y, hue=self.hue,
                    row=self.row, col=self.col, kind=self.kind, estimator=self.estimator,
                    errorbar=self.errorbar, n_boot=self.n_boot,units=self.units,weights=self.weights,
                    order=self.order, hue_order=self.hue_order, row_order=self.row_order, col_order=self.col_order,
                    col_wrap=self.col_wrap, log_scale=self.log_scale,
                     palette=self.palette,
                     legend=self.legend, legend_out=self.legend_out,
                    sharex=self.sharex, sharey=self.sharey, margin_titles=self.margin_titles)
        st.pyplot(plt)

class Stripplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]

        # Required parameters
        self.x = st.selectbox("(sns.stripplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.stripplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.stripplot) hue", [None] + self.columns)

        # Ordering and hue options
        self.order = st.multiselect("(sns.stripplot) order", self.dataset[self.x].unique() if self.x else []) if self.x else None
        self.hue_order = st.multiselect("(sns.stripplot) hue_order", self.dataset[self.hue].unique() if self.hue else []) if self.hue else None

        # Appearance options
        self.jitter = st.selectbox("(sns.stripplot) jitter", self.bool, index=0)
        self.dodge = st.selectbox("(sns.stripplot) dodge", self.bool, index=1)
        self.orient = st.selectbox("(sns.stripplot) orient", [None, 'v', 'h'])
        self.palette = st.selectbox("(sns.stripplot) palette", sns.color_palette().as_hex() + ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.size = st.slider("(sns.stripplot) size", min_value=1, max_value=20, value=5)
        self.edgecolor = st.color_picker("(sns.stripplot) edgecolor", "#000000")
        self.linewidth = st.slider("(sns.stripplot) linewidth", min_value=0, max_value=5, value=0)

        # Scaling and formatting
        self.log_scale = st.selectbox("(sns.stripplot) log_scale", [None, True, False])
        self.native_scale = st.selectbox("(sns.stripplot) native_scale", self.bool)

        # Legend
        self.legend = st.selectbox("(sns.stripplot) legend", ['auto', True, False])

    def plot(self):
        # Plotting with seaborn stripplot
        try:
            sns.stripplot(data=self.dataset,
                          x=self.x, y=self.y, hue=self.hue,
                          order=self.order, hue_order=self.hue_order,
                          jitter=self.jitter, dodge=self.dodge, orient=self.orient,
                          palette=self.palette, size=self.size,
                          edgecolor=self.edgecolor, linewidth=self.linewidth,
                          log_scale=self.log_scale, native_scale=self.native_scale,
                          legend=self.legend)

            st.pyplot(plt)
        except Exception as e:
            st.error(f"An error occurred: {e}")

class Swarmplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        self.x = st.selectbox("(sns.swarmplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.swarmplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.swarmplot) hue", [None] + self.columns)
        self.order = st.multiselect("(sns.swarmplot) order", self.dataset[self.x].unique() if self.x else []) if self.x else None
        self.hue_order = st.multiselect("(sns.swarmplot) hue_order", self.dataset[self.hue].unique() if self.hue else []) if self.hue else None
        self.dodge = st.selectbox("(sns.swarmplot) dodge", self.bool, index=0)
        self.orient = st.selectbox("(sns.swarmplot) orient", [None, 'v', 'h'])
        self.color = st.color_picker("(sns.swarmplot) color", "#000000")
        self.palette = st.selectbox("(sns.swarmplot) palette",['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.size = st.slider("(sns.swarmplot) size", min_value=1, max_value=20, value=5)
        self.edgecolor = st.color_picker("(sns.swarmplot) edgecolor", "#000000")
        self.linewidth = st.slider("(sns.swarmplot) linewidth", min_value=0, max_value=5, value=0)
        self.log_scale = st.selectbox("(sns.swarmplot) log_scale", [None, True, False])
        self.native_scale = st.selectbox("(sns.swarmplot) native_scale", self.bool)
        self.legend = st.selectbox("(sns.swarmplot) legend", ['auto', True, False])
        self.warn_thresh = st.slider("(sns.swarmplot) warn_thresh", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

    def plot(self):
        # Plotting with seaborn swarmplot
        try:
            sns.swarmplot(data=self.dataset,
                          x=self.x, y=self.y, hue=self.hue,
                          order=self.order, hue_order=self.hue_order,
                          dodge=self.dodge, orient=self.orient,
                          color=self.color, palette=self.palette, size=self.size,
                          edgecolor=self.edgecolor, linewidth=self.linewidth,
                          log_scale=self.log_scale, native_scale=self.native_scale,
                          legend=self.legend, warn_thresh=self.warn_thresh)

            st.pyplot(plt)
        except Exception as e:
            st.error(f"An error occurred: {e}")

class Boxplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        
        # Required parameters
        self.x = st.selectbox("(sns.boxplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.boxplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.boxplot) hue", [None] + self.columns)

        # Ordering options
        self.order = st.multiselect("(sns.boxplot) order", self.dataset[self.x].unique() if self.x else []) if self.x else None
        self.hue_order = st.multiselect("(sns.boxplot) hue_order", self.dataset[self.hue].unique() if self.hue else []) if self.hue else None

        # Appearance options
        self.orient = st.selectbox("(sns.boxplot) orient", [None, 'v', 'h'])
        self.color = st.color_picker("(sns.boxplot) color", "#000000")
        self.palette = st.selectbox("(sns.boxplot) palette",['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.saturation = st.slider("(sns.boxplot) saturation", min_value=0.0, max_value=1.0, value=0.75, step=0.05)
        self.fill = st.selectbox("(sns.boxplot) fill", self.bool, index=0)
        self.dodge = st.selectbox("(sns.boxplot) dodge", [True, False, 'auto'], index=2)
        self.width = st.slider("(sns.boxplot) width", min_value=0.1, max_value=1.0, value=0.8, step=0.1)
        self.gap = st.slider("(sns.boxplot) gap", min_value=0.0, max_value=1.0, value=0.0, step=0.05)

        # Boxplot statistical parameters
        self.whis = st.slider("(sns.boxplot) whis", min_value=0.1, max_value=5.0, value=1.5, step=0.1)
        self.linecolor = st.color_picker("(sns.boxplot) linecolor", "#000000")
        self.linewidth = st.slider("(sns.boxplot) linewidth", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
        self.fliersize = st.slider("(sns.boxplot) fliersize", min_value=1, max_value=10, value=5, step=1)

        # Scaling and formatting
        self.log_scale = st.selectbox("(sns.boxplot) log_scale", [None, True, False])
        self.native_scale = st.selectbox("(sns.boxplot) native_scale", self.bool)

        # Legend
        self.legend = st.selectbox("(sns.boxplot) legend", ['auto', True, False])

    def plot(self):
        # Plotting with seaborn boxplot
        try:
            sns.boxplot(data=self.dataset,
                        x=self.x, y=self.y, hue=self.hue,
                        order=self.order, hue_order=self.hue_order, orient=self.orient,
                        color=self.color, palette=self.palette, saturation=self.saturation,
                        fill=self.fill, dodge=self.dodge, width=self.width, gap=self.gap,
                        whis=self.whis, linecolor=self.linecolor, linewidth=self.linewidth,
                        fliersize=self.fliersize,log_scale=self.log_scale,
                        native_scale=self.native_scale, legend=self.legend)
            st.pyplot(plt)
        except Exception as e:
            st.error(f"An error occurred: {e}")


class ViolinPlot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool = [True, False]
        
        # Required parameters
        self.x = st.selectbox("(sns.violinplot) x", [None] + self.columns)
        self.y = st.selectbox("(sns.violinplot) y", [None] + self.columns)
        self.hue = st.selectbox("(sns.violinplot) hue", [None] + self.columns)

        # Ordering options
        self.order = st.multiselect("(sns.violinplot) order", self.dataset[self.x].unique() if self.x else []) if self.x else None
        self.hue_order = st.multiselect("(sns.violinplot) hue_order", self.dataset[self.hue].unique() if self.hue else []) if self.hue else None

        # Appearance options
        self.orient = st.selectbox("(sns.violinplot) orient", [None, 'v', 'h'])
        self.color = st.color_picker("(sns.violinplot) color", "#000000")
        self.palette = st.selectbox("(sns.violinplot) palette",['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.saturation = st.slider("(sns.violinplot) saturation", min_value=0.0, max_value=1.0, value=0.75, step=0.05)
        self.fill = st.selectbox("(sns.violinplot) fill", self.bool, index=0)
        self.inner = st.selectbox("(sns.violinplot) inner", ['box', 'quartile', 'point', 'stick', None])
        self.split = st.selectbox("(sns.violinplot) split", self.bool, index=0)
        self.width = st.slider("(sns.violinplot) width", min_value=0.1, max_value=1.0, value=0.8, step=0.1)
        self.dodge = st.selectbox("(sns.violinplot) dodge", [True, False, 'auto'], index=2)
        self.gap = st.slider("(sns.violinplot) gap", min_value=0.0, max_value=1.0, value=0.0, step=0.05)
        self.linewidth = st.slider("(sns.violinplot) linewidth", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
        self.linecolor = st.color_picker("(sns.violinplot) linecolor", "#000000")

        # Kernel Density Estimation parameters
        self.cut = st.slider("(sns.violinplot) cut", min_value=0, max_value=10, value=2, step=1)
        self.gridsize = st.slider("(sns.violinplot) gridsize", min_value=50, max_value=200, value=100, step=10)
        self.bw_method = st.selectbox("(sns.violinplot) bw_method", ['scott', 'silverman', None])
        self.bw_adjust = st.slider("(sns.violinplot) bw_adjust", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

        # Scaling and formatting
        self.density_norm = st.selectbox("(sns.violinplot) density_norm", ['area', 'count', 'width'])
        self.common_norm = st.selectbox("(sns.violinplot) common_norm", self.bool)
        self.log_scale = st.selectbox("(sns.violinplot) log_scale", [None, True, False])
        self.native_scale = st.selectbox("(sns.violinplot) native_scale", self.bool)
        self.legend = st.selectbox("(sns.violinplot) legend", ['auto', True, False])

    def plot(self):
        # Plotting with seaborn violinplot
        try:
            sns.violinplot(data=self.dataset,
                           x=self.x, y=self.y, hue=self.hue,
                           order=self.order, hue_order=self.hue_order, orient=self.orient,
                           color=self.color, palette=self.palette, saturation=self.saturation,
                           fill=self.fill, inner=self.inner, split=self.split, width=self.width,
                           dodge=self.dodge, gap=self.gap, linewidth=self.linewidth, linecolor=self.linecolor,
                           cut=self.cut, gridsize=self.gridsize, bw_method=self.bw_method, bw_adjust=self.bw_adjust,
                           density_norm=self.density_norm, common_norm=self.common_norm, log_scale=self.log_scale,
                           native_scale=self.native_scale, legend=self.legend)
            st.pyplot(plt)
        except Exception as e:
            st.error(f"An error occurred: {e}")

class Boxenplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool_options = [True, False]
        self.none_or_bool = [None, True, False]
        
        st.header("Seaborn Boxen Plot Configuration")
        
        # Required parameters
        st.subheader("Axes Parameters")
        self.x = st.selectbox("X-axis", [None] + self.columns)
        self.y = st.selectbox("Y-axis", [None] + self.columns)
        self.hue = st.selectbox("Hue", [None] + self.columns)
        
        # Order parameters
        st.subheader("Order Parameters")
        self.order = st.multiselect("Order", self.get_unique_values(self.x))
        self.hue_order = st.multiselect("Hue Order", self.get_unique_values(self.hue))
        self.orient = st.selectbox("Orientation", [None, 'v', 'h'])
        
        # Color parameters
        st.subheader("Color Parameters")
        self.color = st.color_picker("Color", value="#69b3a2")
        self.palette = st.selectbox(
            "Palette", 
            [None, 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'] + sorted(sns.palettes.SEABORN_PALETTES.keys())
        )
        self.saturation = st.slider("Saturation", min_value=0.0, max_value=1.0, value=0.75)
        self.fill = st.selectbox("Fill", self.bool_options, index=0)
        
        # Boxen-specific parameters
        st.subheader("Boxen Specific Parameters")
        self.width = st.slider("Width", min_value=0.1, max_value=2.0, value=0.8)
        self.dodge = st.selectbox("Dodge", self.none_or_bool, index=1 if self.hue else 0)
        self.gap = st.slider("Gap", min_value=0.0, max_value=1.0, value=0.0)
        self.linewidth = st.slider("Line Width", min_value=0.0, max_value=5.0, value=1.0)
        self.linecolor = st.color_picker("Line Color", value="#000000")
        self.width_method = st.selectbox("Width Method", ['linear', 'exponential'])
        self.k_depth = st.selectbox("K Depth", ['tukey', 'proportion', 'trustworthy', 'full'])
        self.outlier_prop = st.slider("Outlier Proportion", min_value=0.001, max_value=0.1, value=0.007, step=0.001)
        self.trust_alpha = st.slider("Trust Alpha", min_value=0.01, max_value=0.1, value=0.05, step=0.01)
        self.showfliers = st.selectbox("Show Fliers", self.bool_options, index=1)
        
        # Scale and formatting
        st.subheader("Scale and Formatting")
        self.log_scale = st.selectbox("Log Scale", [None, True, False], index=0)
        self.native_scale = st.selectbox("Native Scale", self.bool_options, index=1)
        self.formatter = st.text_input("Formatter", value="")
        
        # Legend and Axes
        st.subheader("Legend and Axes")
        self.legend = st.selectbox("Legend", ['auto', True, False], index=0)
    
    def get_unique_values(self, column):
        if column:
            unique_vals = self.dataset[column].unique()
            return sorted(unique_vals)
        return []
    
    def plot(self):
        try:
            plt.figure(figsize=(10, 6))
            sns.boxenplot(
                data=self.dataset,
                x=self.x,
                y=self.y,
                hue=self.hue,
                order=self.order if self.order else None,
                hue_order=self.hue_order if self.hue_order else None,
                orient=self.orient,
                color=self.color if not self.palette else None,
                palette=self.palette,
                saturation=self.saturation,
                fill=self.fill,
                width=self.width,
                dodge=self.dodge if self.hue else False,
                gap=self.gap,
                linewidth=self.linewidth,
                linecolor=self.linecolor,
                width_method=self.width_method,
                k_depth=self.k_depth,
                outlier_prop=self.outlier_prop,
                trust_alpha=self.trust_alpha,
                showfliers=self.showfliers,
                log_scale=self.log_scale,
                native_scale=self.native_scale,
                legend=self.legend
            )
            
            plt.tight_layout()
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")

class Pointplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool_options = [True, False]
        self.none_or_bool = [None, True, False]
        
        st.header("Seaborn Point Plot Configuration")
        
        # Axes Parameters
        st.subheader("Axes Parameters")
        self.x = st.selectbox("X-axis", [None] + self.columns)
        self.y = st.selectbox("Y-axis", [None] + self.columns)
        self.hue = st.selectbox("Hue", [None] + self.columns)
        
        # Order Parameters
        st.subheader("Order Parameters")
        self.order = st.multiselect("Order", self.get_unique_values(self.x))
        self.hue_order = st.multiselect("Hue Order", self.get_unique_values(self.hue))
        self.orient = st.selectbox("Orientation", [None, 'v', 'h'])
        
        # Estimator and Error Bar
        st.subheader("Estimator and Error Bar")
        self.estimator = st.selectbox("Estimator", ['mean', 'median', 'sum', 'std', 'var', 'min', 'max'])
        self.errorbar_type = st.selectbox("Errorbar Type", ['ci', 'pi', 'se', 'sd'])
        self.errorbar_value = st.number_input("Errorbar Value", value=95, step=1)
        self.n_boot = st.slider("Number of Bootstrap Iterations", min_value=100, max_value=5000, value=1000, step=100)
        
        # Units and Weights
        st.subheader("Units and Weights")
        self.units = st.selectbox("Units", [None] + self.columns)
        self.weights = st.selectbox("Weights", [None] + self.columns)
        
        # Aesthetic Parameters
        st.subheader("Aesthetic Parameters")
        self.color = st.color_picker("Color", value="#000000")
        self.palette = st.selectbox(
            "Palette", 
            [None, 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'] + sorted(sns.palettes.SEABORN_PALETTES.keys())
        )
        self.markers = st.text_input("Markers", value="o")
        self.linestyles = st.text_input("Linestyles", value="-")
        self.dodge = st.selectbox("Dodge", self.bool_options)
        self.capsize = st.slider("Capsize", min_value=0.0, max_value=1.0, value=0.0)
        
        # Scaling and Formatting
        st.subheader("Scaling and Formatting")
        self.log_scale = st.selectbox("Log Scale", [None, True, False])
        self.native_scale = st.selectbox("Native Scale", self.bool_options)
        
        # Legend
        st.subheader("Legend")
        self.legend = st.selectbox("Legend", ['auto', True, False])
    
    def get_unique_values(self, column):
        if column:
            unique_vals = self.dataset[column].unique()
            return sorted(unique_vals)
        return []
    
    def plot(self):
        try:
            plt.figure(figsize=(10, 6))
            sns.pointplot(
                data=self.dataset,
                x=self.x,
                y=self.y,
                hue=self.hue,
                order=self.order if self.order else None,
                hue_order=self.hue_order if self.hue_order else None,
                estimator=self.estimator,
                errorbar=(self.errorbar_type, self.errorbar_value),
                n_boot=self.n_boot,
                units=self.units,
                weights=self.weights,
                color=self.color if not self.palette else None,
                palette=self.palette,
                markers=self.markers,
                linestyles=self.linestyles,
                dodge=self.dodge,
                log_scale=self.log_scale,
                native_scale=self.native_scale,
                orient=self.orient,
                capsize=self.capsize,
                legend=self.legend
            )
            
            plt.tight_layout()
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")


class Barplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool_options = [True, False]
        
        st.header("Seaborn Bar Plot Configuration")
        
        # Axes Parameters
        st.subheader("Axes Parameters")
        self.x = st.selectbox("X-axis", [None] + self.columns)
        self.y = st.selectbox("Y-axis", [None] + self.columns)
        self.hue = st.selectbox("Hue", [None] + self.columns)
        
        # Order Parameters
        st.subheader("Order Parameters")
        self.order = st.multiselect("Order", self.get_unique_values(self.x))
        self.hue_order = st.multiselect("Hue Order", self.get_unique_values(self.hue))
        self.orient = st.selectbox("Orientation", [None, 'v', 'h'])
        
        # Estimator and Error Bar
        st.subheader("Estimator and Error Bar")
        self.estimator = st.selectbox("Estimator", ['mean', 'median', 'sum', 'std', 'var', 'min', 'max'])
        self.errorbar_type = st.selectbox("Errorbar Type", ['ci', 'pi', 'se', 'sd'])
        self.errorbar_value = st.number_input("Errorbar Value", value=95, step=1)
        self.n_boot = st.slider("Number of Bootstrap Iterations", min_value=100, max_value=5000, value=1000, step=100)
        
        # Units and Weights
        st.subheader("Units and Weights")
        self.units = st.selectbox("Units", [None] + self.columns)
        self.weights = st.selectbox("Weights", [None] + self.columns)
        
        # Aesthetic Parameters
        st.subheader("Aesthetic Parameters")
        self.color = st.color_picker("Color", value="#000000")
        self.palette = st.selectbox(
            "Palette", 
            [None, 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'] + sorted(sns.palettes.SEABORN_PALETTES.keys())
        )
        self.saturation = st.slider("Saturation", min_value=0.0, max_value=1.0, value=0.75)
        self.fill = st.selectbox("Fill", self.bool_options)
        self.width = st.slider("Bar Width", min_value=0.1, max_value=1.0, value=0.8)
        self.dodge = st.selectbox("Dodge", self.bool_options)
        self.gap = st.slider("Gap", min_value=0, max_value=5, value=0)
        self.capsize = st.slider("Capsize", min_value=0.0, max_value=1.0, value=0.0)
        
        # Scaling and Formatting
        st.subheader("Scaling and Formatting")
        self.log_scale = st.selectbox("Log Scale", [None, True, False])
        self.native_scale = st.selectbox("Native Scale", self.bool_options)
        
        # Legend
        st.subheader("Legend")
        self.legend = st.selectbox("Legend", ['auto', True, False])
    
    def get_unique_values(self, column):
        if column:
            unique_vals = self.dataset[column].unique()
            return sorted(unique_vals)
        return []
    
    def plot(self):
        try:
            plt.figure(figsize=(10, 6))
            sns.barplot(
                data=self.dataset,
                x=self.x,
                y=self.y,
                hue=self.hue,
                order=self.order if self.order else None,
                hue_order=self.hue_order if self.hue_order else None,
                estimator=self.estimator,
                errorbar=(self.errorbar_type, self.errorbar_value),
                n_boot=self.n_boot,
                units=self.units,
                weights=self.weights,
                color=self.color if not self.palette else None,
                palette=self.palette,
                saturation=self.saturation,
                fill=self.fill,
                width=self.width,
                dodge=self.dodge,
                gap=self.gap,
                log_scale=self.log_scale,
                native_scale=self.native_scale,
                orient=self.orient,
                capsize=self.capsize,
                legend=self.legend
            )
            
            plt.tight_layout()
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")


class Countplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool_options = [True, False]
        
        st.header("Seaborn Count Plot Configuration")
        
        # Axes Parameters
        st.subheader("Axes Parameters")
        self.x = st.selectbox("X-axis", [None] + self.columns)
        self.y = st.selectbox("Y-axis", [None] + self.columns)
        self.hue = st.selectbox("Hue", [None] + self.columns)
        
        # Order Parameters
        st.subheader("Order Parameters")
        self.order = st.multiselect("Order", self.get_unique_values(self.x))
        self.hue_order = st.multiselect("Hue Order", self.get_unique_values(self.hue))
        self.orient = st.selectbox("Orientation", [None, 'v', 'h'])
        
        # Aesthetic Parameters
        st.subheader("Aesthetic Parameters")
        self.color = st.color_picker("Color", value="#000000")
        self.palette = st.selectbox(
            "Palette", 
            [None, 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'] + sorted(sns.palettes.SEABORN_PALETTES.keys())
        )
        self.saturation = st.slider("Saturation", min_value=0.0, max_value=1.0, value=0.75)
        self.fill = st.selectbox("Fill", self.bool_options)
        self.width = st.slider("Bar Width", min_value=0.1, max_value=1.0, value=0.8)
        self.dodge = st.selectbox("Dodge", self.bool_options)
        self.gap = st.slider("Gap", min_value=0, max_value=5, value=0)
        
        # Scaling and Formatting
        st.subheader("Scaling and Formatting")
        self.log_scale = st.selectbox("Log Scale", [None, True, False])
        self.native_scale = st.selectbox("Native Scale", self.bool_options)
        
        # Legend
        st.subheader("Legend")
        self.legend = st.selectbox("Legend", ['auto', True, False])

        # Statistical Parameters
        st.subheader("Statistical Parameters")
        self.stat = st.selectbox("Stat", ['count', 'percent', 'probability', 'proportion'])

    def get_unique_values(self, column):
        if column:
            unique_vals = self.dataset[column].unique()
            return sorted(unique_vals)
        return []
    
    def plot(self):
        try:
            plt.figure(figsize=(10, 6))
            sns.countplot(
                data=self.dataset,
                x=self.x,
                y=self.y,
                hue=self.hue,
                order=self.order if self.order else None,
                hue_order=self.hue_order if self.hue_order else None,
                color=self.color if not self.palette else None,
                palette=self.palette,
                saturation=self.saturation,
                fill=self.fill,
                width=self.width,
                dodge=self.dodge,
                gap=self.gap,
                log_scale=self.log_scale,
                native_scale=self.native_scale,
                orient=self.orient,
                legend=self.legend,
                stat=self.stat
            )
            
            plt.tight_layout()
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")


class Lmplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        self.bool_options = [True, False]

        st.header("Seaborn LM Plot Configuration")

        # Required Parameters
        st.subheader("Required Parameters")
        self.x = st.selectbox("X-axis", [None] + self.columns)
        self.y = st.selectbox("Y-axis", [None] + self.columns)
        self.hue = st.selectbox("Hue", [None] + self.columns)

        # Facet Parameters
        st.subheader("Facet Parameters")
        self.col = st.selectbox("Column (Facet)", [None] + self.columns)
        self.row = st.selectbox("Row (Facet)", [None] + self.columns)
        self.col_wrap = st.slider("Column Wrap", min_value=1, max_value=10, value=4) if self.col else None

        # Order Parameters
        st.subheader("Order Parameters")
        self.hue_order = st.multiselect("Hue Order", self.get_unique_values(self.hue))
        self.col_order = st.multiselect("Column Order", self.get_unique_values(self.col))
        self.row_order = st.multiselect("Row Order", self.get_unique_values(self.row))

        # Plot Appearance
        st.subheader("Plot Appearance")
        self.palette = st.selectbox("Palette", [None, 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'] + sorted(sns.palettes.SEABORN_PALETTES.keys()))
        self.markers = st.text_input("Markers", value="o")
        self.height = st.slider("Height", min_value=1.0, max_value=10.0, value=5.0)
        self.aspect = st.slider("Aspect Ratio", min_value=0.5, max_value=2.0, value=1.0)
        self.sharex = st.selectbox("Share X Axis", [None, True, False])
        self.sharey = st.selectbox("Share Y Axis", [None, True, False])
        self.legend = st.selectbox("Legend", [True, False])
        self.legend_out = st.selectbox("Legend Outside", [None, True, False])

        # Statistical and Estimation Parameters
        st.subheader("Statistical and Estimation Parameters")
        self.x_estimator = st.selectbox("X Estimator", [None, 'mean', 'median', 'sum', 'std', 'var', 'min', 'max'])
        self.x_bins = st.slider("X Bins", min_value=1, max_value=50, value=10)
        self.x_ci = st.selectbox("X Confidence Interval", [None, 'ci', 'pi', 'se', 'sd', 'range', 'percentile', 'var'], index=0)
        self.scatter = st.selectbox("Show Scatter", self.bool_options)
        self.fit_reg = st.selectbox("Fit Regression", self.bool_options)
        self.ci = st.slider("Confidence Interval", min_value=0, max_value=100, value=95)
        self.n_boot = st.slider("Number of Bootstrap Samples", min_value=100, max_value=5000, value=1000, step=100)
        self.units = st.selectbox("Units", [None] + self.columns)
        self.seed = st.number_input("Random Seed", value=0)
        self.order = st.slider("Polynomial Order", min_value=1, max_value=5, value=1)
        self.logistic = st.selectbox("Logistic Regression", self.bool_options)
        self.lowess = st.selectbox("Lowess Smoothing", self.bool_options)
        self.robust = st.selectbox("Robust Regression", self.bool_options)
        self.logx = st.selectbox("Logarithmic X Scale", self.bool_options)

    def get_unique_values(self, column):
        if column:
            unique_vals = self.dataset[column].unique()
            return sorted(unique_vals)
        return []

    def plot(self):
        try:
            if self.x and self.y:
                sns.lmplot(
                    data=self.dataset,
                    x=self.x,
                    y=self.y,
                    hue=self.hue,
                    col=self.col,
                    row=self.row,
                    palette=self.palette,
                    col_wrap=self.col_wrap,
                    height=self.height,
                    aspect=self.aspect,
                    markers=self.markers,
                    sharex=self.sharex,
                    sharey=self.sharey,
                    hue_order=self.hue_order if self.hue else None,
                    col_order=self.col_order if self.col else None,
                    row_order=self.row_order if self.row else None,
                    legend=self.legend,
                    legend_out=self.legend_out,
                    x_estimator=None if self.x_estimator == "None" else self.x_estimator,
                    x_bins=self.x_bins,
                    x_ci=self.x_ci,
                    scatter=self.scatter,
                    fit_reg=self.fit_reg,
                    ci=self.ci,
                    n_boot=self.n_boot,
                    units=self.units,
                    seed=self.seed,
                    order=self.order,
                    logistic=self.logistic,
                    lowess=self.lowess,
                    robust=self.robust,
                    logx=self.logx
                )
                st.pyplot(plt.gcf())
            else:
                st.error("Please select X and Y variables")
        except Exception as e:
            st.error(f"An error occurred: {e}")



class Regplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        
        st.header("Seaborn Reg Plot Configuration")

        # Required Parameters
        st.subheader("Required Parameters")
        self.x = st.selectbox("X-axis", [None] + self.columns)
        self.y = st.selectbox("Y-axis", [None] + self.columns)
        
        # Statistical and Estimation Parameters
        st.subheader("Statistical and Estimation Parameters")
        self.x_estimator = st.selectbox("X Estimator", [None, 'mean', 'median', 'sum', 'std', 'var', 'min', 'max'])
        self.x_bins = st.slider("X Bins", min_value=1, max_value=50, value=10)
        self.x_ci = st.selectbox("X Confidence Interval", [None, 'ci', 'pi', 'se', 'sd', 'range', 'percentile', 'var'], index=0)
        self.scatter = st.selectbox("Show Scatter", [True, False])
        self.fit_reg = st.selectbox("Fit Regression", [True, False])
        self.ci = st.slider("Confidence Interval", min_value=0, max_value=100, value=95)
        self.n_boot = st.slider("Number of Bootstrap Samples", min_value=100, max_value=5000, value=1000, step=100)
        self.units = st.selectbox("Units", [None] + self.columns)
        self.seed = st.number_input("Random Seed", value=0)
        self.order = st.slider("Polynomial Order", min_value=1, max_value=5, value=1)
        self.logistic = st.selectbox("Logistic Regression", [True, False])
        self.lowess = st.selectbox("Lowess Smoothing", [True, False])
        self.robust = st.selectbox("Robust Regression", [True, False])
        self.logx = st.selectbox("Logarithmic X Scale", [True, False])
        self.x_partial = st.selectbox("X Partial", [None] + self.columns)
        self.y_partial = st.selectbox("Y Partial", [None] + self.columns)
        self.truncate = st.selectbox("Truncate Data", [True, False])
        self.dropna = st.selectbox("Drop NA Values", [True, False])
        self.x_jitter = st.slider("X Jitter", min_value=0.0, max_value=1.0, value=0.0)
        self.y_jitter = st.slider("Y Jitter", min_value=0.0, max_value=1.0, value=0.0)
        self.label = st.text_input("Label")
        self.color = st.color_picker("Color", "#000000")
        self.marker = st.text_input("Marker", value='o')


    def plot(self):
        try:

            sns.regplot(
                data=self.dataset,
                x=self.x,
                y=self.y,
                x_estimator=None if self.x_estimator == "None" else self.x_estimator,
                x_bins=self.x_bins,
                x_ci=self.x_ci,
                scatter=self.scatter,
                fit_reg=self.fit_reg,
                ci=self.ci,
                n_boot=self.n_boot,
                units=self.units,
                seed=self.seed,
                order=self.order,
                logistic=self.logistic,
                lowess=self.lowess,
                robust=self.robust,
                logx=self.logx,
                x_partial=self.x_partial,
                y_partial=self.y_partial,
                truncate=self.truncate,
                dropna=self.dropna,
                x_jitter=self.x_jitter,
                y_jitter=self.y_jitter,
                label=self.label,
                color=self.color,
                marker=self.marker,
                ax=None  # Ax is not handled in this example
            )
            st.pyplot(plt)
        except Exception as e:
            st.error(f"An error occurred: {e}")


class Residplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)
        
        st.header("Seaborn Residual Plot Configuration")

        # Required Parameters
        st.subheader("Required Parameters")
        self.x = st.selectbox("X-axis", [None] + self.columns)
        self.y = st.selectbox("Y-axis", [None] + self.columns)

        # Statistical Parameters
        st.subheader("Statistical Parameters")
        self.x_partial = st.selectbox("X Partial", [None] + self.columns)
        self.y_partial = st.selectbox("Y Partial", [None] + self.columns)
        self.lowess = st.selectbox("Lowess Smoothing", [True, False])
        self.order = st.slider("Polynomial Order", min_value=1, max_value=5, value=1)
        self.robust = st.selectbox("Robust Regression", [True, False])
        self.dropna = st.selectbox("Drop NA Values", [True, False])

        # Aesthetics
        st.subheader("Aesthetics")
        self.label = st.text_input("Label")
        self.color = st.color_picker("Color", "#000000")


    def plot(self):
        try:

            sns.residplot(
                data=self.dataset,
                x=self.x,
                y=self.y,
                x_partial=self.x_partial,
                y_partial=self.y_partial,
                lowess=self.lowess,
                order=self.order,
                robust=self.robust,
                dropna=self.dropna,
                label=self.label,
                color=self.color,
                ax=None  # Ax is not handled in this example
            )
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")



class Heatmap:
    def __init__(self, dataset):
        self.dataset = dataset.select_dtypes(exclude=['object','datetime','timedelta','category'])
        self.columns=list(self.dataset.columns)
        self.dataset1=dataset
        
        st.header("Seaborn Heatmap Configuration")


        st.subheader("Heatmap Parameters")
        self.vmin = st.number_input("Minimum Value (vmin)", value=None, format="%.2f")
        self.vmax = st.number_input("Maximum Value (vmax)", value=None, format="%.2f")
        self.cmap = st.selectbox("Colormap (cmap)", ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.center = st.number_input("Center Value (center)", value=None, format="%.2f")
        self.robust = st.selectbox("Robust Scaling", [True, False])
        self.annot = st.selectbox("Annotations (annot)", [True, False, None])
        self.fmt = st.text_input("Annotation Format (fmt)", value='.2g')
        self.annot_kws = st.text_area("Annotation Keyword Arguments (annot_kws as dict)", value="")
        self.linewidths = st.slider("Line Widths (linewidths)", min_value=0, max_value=10, value=0)
        self.linecolor = st.color_picker("Line Color (linecolor)", "#FFFFFF")
        self.cbar = st.selectbox("Colorbar (cbar)", [True, False])
        self.square = st.selectbox("Square Aspect Ratio (square)", [True, False])
        self.xticklabels = st.selectbox("X-tick Labels (xticklabels)", ['auto', 'None'] + list(self.dataset.columns))
        self.yticklabels = st.selectbox("Y-tick Labels (yticklabels)", ['auto', 'None'] + list(self.dataset.index))
        self.mask = st.selectbox("Mask (mask)", [True, False, None])


    def plot(self):
        try:
            sns.heatmap(
                data=self.dataset,
                vmin=self.vmin,
                vmax=self.vmax,
                cmap=self.cmap,
                center=self.center,
                robust=self.robust,
                annot=self.annot,
                fmt=self.fmt,
                linewidths=self.linewidths,
                linecolor=self.linecolor,
                cbar=self.cbar,
                square=self.square,
                xticklabels=self.xticklabels,
                yticklabels=self.yticklabels,
                mask=self.mask,
            )
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")

class Jointplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)

        st.header("Seaborn Jointplot Configuration")

        # Required parameters
        st.subheader("Data Parameters")
        self.x = st.selectbox("x-axis", self.columns)
        self.y = st.selectbox("y-axis", self.columns)
        self.hue = st.selectbox("Hue", [None] + self.columns)

        # Plot kind
        self.kind = st.selectbox("Kind of Plot", ['scatter', 'reg', 'resid', 'kde', 'hex'])

        # Plot size and ratio
        st.subheader("Plot Dimensions")
        self.height = st.slider("Height", min_value=4.0, max_value=12.0, value=6.0, step=0.5)
        self.ratio = st.slider("Ratio", min_value=1, max_value=10, value=5)
        self.space = st.slider("Space between plots", min_value=0.1, max_value=1.0, value=0.2, step=0.1)

        # Axes limits
        st.subheader("Axes Limits")
        self.xlim = st.text_input("x-axis limits (comma-separated, e.g., 0,100)", value=None)
        self.ylim = st.text_input("y-axis limits (comma-separated, e.g., 0,100)", value=None)

        # Aesthetics
        st.subheader("Aesthetics")
        self.palette = st.selectbox("Palette",['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.hue_order = st.multiselect("Hue Order", self.dataset[self.hue].unique() if self.hue else [])
        self.hue_norm = st.text_input("Hue Norm", value=None)
        self.marginal_ticks = st.selectbox("Marginal Ticks", [False, True])

        # Additional keyword arguments
        st.subheader("Additional Keyword Arguments")
        self.joint_kws = st.text_area("Jointplot Keyword Arguments (joint_kws as dict)", value="")
        self.marginal_kws = st.text_area("Marginal Keyword Arguments (marginal_kws as dict)", value="")
        self.dropna = st.selectbox("Drop NA Values", [True, False])

    def plot(self):
        try:
            # Convert text inputs for xlim and ylim to tuple of floats
            xlim = tuple(map(float, self.xlim.split(','))) if self.xlim else None
            ylim = tuple(map(float, self.ylim.split(','))) if self.ylim else None

            # Convert text inputs for kwargs
            joint_kws = eval(self.joint_kws) if self.joint_kws else {}
            marginal_kws = eval(self.marginal_kws) if self.marginal_kws else {}
            hue_norm = eval(self.hue_norm) if self.hue_norm else None

            # Creating the jointplot
            sns.jointplot(data=self.dataset,
                          x=self.x, y=self.y, hue=self.hue,
                          kind=self.kind, height=self.height, ratio=self.ratio, space=self.space,
                          xlim=xlim, ylim=ylim, palette=self.palette,
                          hue_order=self.hue_order, hue_norm=hue_norm,
                          marginal_ticks=self.marginal_ticks, dropna=self.dropna,
                          joint_kws=joint_kws, marginal_kws=marginal_kws)
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")


class Pairplot:
    def __init__(self, dataset):
        self.dataset = dataset
        self.columns = list(self.dataset.columns)

        st.header("Seaborn Pairplot Configuration")

        # Data parameters
        st.subheader("Data Parameters")
        self.hue = st.selectbox("Hue", [None] + self.columns)
        self.hue_order = st.multiselect("Hue Order", self.dataset[self.hue].unique() if self.hue else [])

        # Variables to plot
        st.subheader("Variables to Plot")
        self.vars = st.multiselect("Variables to Plot", self.columns)
        self.x_vars = st.multiselect("x Variables", self.columns)
        self.y_vars = st.multiselect("y Variables", self.columns)

        # Plot type
        st.subheader("Plot Type")
        self.kind = st.selectbox("Kind of Plot", ['scatter', 'kde', 'reg'])

        # Diagonal plot type
        self.diag_kind = st.selectbox("Diagonal Kind", ['auto', 'hist', 'kde', 'none'])

        # Plot aesthetics
        st.subheader("Plot Aesthetics")
        self.palette = st.selectbox("Palette",['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.markers = st.text_input("Markers (comma-separated, e.g., o,s,D)", value="o")
        self.height = st.slider("Height", min_value=1.0, max_value=10.0, value=2.5, step=0.5)
        self.aspect = st.slider("Aspect Ratio", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
        self.corner = st.selectbox("Corner", [False, True])
        self.dropna = st.selectbox("Drop NA Values", [True, False])

        # Additional keyword arguments
        st.subheader("Additional Keyword Arguments")
        self.plot_kws = st.text_area("Plot Keyword Arguments (plot_kws as dict)", value="")
        self.diag_kws = st.text_area("Diagonal Keyword Arguments (diag_kws as dict)", value="")
        self.grid_kws = st.text_area("Grid Keyword Arguments (grid_kws as dict)", value="")

    def plot(self):
        try:
            # Convert text inputs for markers and kwargs
            markers = self.markers.split(',') if self.markers else None
            plot_kws = eval(self.plot_kws) if self.plot_kws else {}
            diag_kws = eval(self.diag_kws) if self.diag_kws else {}
            grid_kws = eval(self.grid_kws) if self.grid_kws else {}

            # Creating the pairplot
            sns.pairplot(data=self.dataset,
                         hue=self.hue, hue_order=self.hue_order, palette=self.palette,
                         vars=self.vars, x_vars=self.x_vars, y_vars=self.y_vars,
                         kind=self.kind, diag_kind=self.diag_kind, markers=markers,
                         height=self.height, aspect=self.aspect, corner=self.corner,
                         dropna=self.dropna, plot_kws=plot_kws, diag_kws=diag_kws, grid_kws=grid_kws)
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
class Matplotlib:
    def __init__(self, dataset):
        self.dataset = dataset
    def allPlots(self,plot_types,col2):
        with col2:
            # Input parameters for plots
                x_axis_data = st.selectbox("Select x-axis data", self.dataset.columns)
                y_axis_data = st.selectbox("Select y-axis data", self.dataset.columns)
                color = st.color_picker("Select color")
                linestyle = st.selectbox("Select line style", ['-', '--', '-.', ':'])
                linewidth = st.slider("Select line width", 0.5, 5.0, 1.5)
                marker = st.selectbox("Select marker style", ['o', 's', '^', 'D', 'None'])
                markersize = st.slider("Select marker size", 1, 10, 5)
                s = st.slider("Select marker size (scatter)", 10, 200, 50)
            
                title, xlabel, ylabel, alpha = self.properties()

                if plot_types=='Line Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.plot(x, y, color=color, linestyle=linestyle, linewidth=linewidth, marker=marker, markersize=markersize, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Error Bar Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    yerr = st.number_input("Enter y-error", value=0.1)
                    xerr = st.number_input("Enter x-error", value=0.1)
                    fmt = st.selectbox("Select format string", ['-', '--', '-.', ':'])
                    ecolor = st.color_picker("Select error bar color")
                    elinewidth = st.slider("Select error bar line width", 0.5, 5.0, 1.5)
                    capsize = st.slider("Select error bar cap size", 0, 10, 2)
                    plt.figure()
                    plt.errorbar(x, y, yerr=yerr, xerr=xerr, fmt=fmt, ecolor=ecolor, elinewidth=elinewidth, capsize=capsize, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Scatter Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.scatter(x, y, color=color, marker=marker, s=s, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Step Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.step(x, y, color=color, linestyle=linestyle, linewidth=linewidth, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Log-Log Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.loglog(x, y, color=color, linestyle=linestyle, linewidth=linewidth, marker=marker, markersize=markersize, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Semi-Log X Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.semilogx(x, y, color=color, linestyle=linestyle, linewidth=linewidth, marker=marker, markersize=markersize, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Semi-Log Y Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.semilogy(x, y, color=color, linestyle=linestyle, linewidth=linewidth, marker=marker, markersize=markersize, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Fill Between Plot':
                    x = self.dataset[x_axis_data]
                    y1 = self.dataset[y_axis_data]
                    y2 = st.slider("Select second y data for fill", 0, len(self.dataset.columns) - 1, 1)
                    y2_data = self.dataset[self.dataset.columns[y2]]
                    plt.figure()
                    plt.fill_between(x, y1, y2_data, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Fill Between X Plot':
                    x = self.dataset[x_axis_data]
                    y1 = self.dataset[y_axis_data]
                    y2 = st.slider("Select second y data for fill", 0, len(self.dataset.columns) - 1, 1)
                    y2_data = self.dataset[self.dataset.columns[y2]]
                    plt.figure()
                    plt.fill_betweenx(x, y1, y2_data, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Bar Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.bar(x, y, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Horizontal Bar Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.barh(x, y, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Stem Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.stem(x, y, linefmt=color, markerfmt=marker, basefmt=' ')
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Event Plot':
                    positions = st.text_input("Enter positions for event plot (comma-separated)", "1,2,3")
                    positions = list(map(float, positions.split(',')))
                    plt.figure()
                    plt.eventplot(positions, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Pie Chart':
                    sizes = st.text_input("Enter pie chart sizes (comma-separated)", "10,20,30,40")
                    labels = st.text_input("Enter pie chart labels (comma-separated)", "A,B,C,D")
                    sizes = list(map(float, sizes.split(',')))
                    labels = labels.split(',')
                    plt.figure()
                    plt.pie(sizes, labels=labels, colors=[color] * len(sizes), alpha=alpha)
                    plt.title(title)
                    st.pyplot(plt.gcf())

                if plot_types=='Stacked Area Plot':
                    x = self.dataset[x_axis_data]
                    y1 = self.dataset[y_axis_data]
                    y2 = st.slider("Select second y data for stack", 0, len(self.dataset.columns) - 1, 1)
                    y2_data = self.dataset[self.dataset.columns[y2]]
                    plt.figure()
                    plt.stackplot(x, y1, y2_data, colors=[color, 'grey'], alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Broken Barh Plot':
                    data = st.text_input("Enter broken barh data (format: start, width, height; start, width, height)", "0,1,1;2,1,1")
                    data = [list(map(float, item.split(','))) for item in data.split(';')]
                    plt.figure()
                    plt.broken_barh(data, (0, 1), color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Vertical Lines Plot':
                    x = self.dataset[x_axis_data]
                    ymin = st.number_input("Enter ymin for vertical lines", value=0.0)
                    ymax = st.number_input("Enter ymax for vertical lines", value=1.0)
                    plt.figure()
                    plt.vlines(x, ymin, ymax, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Horizontal Lines Plot':
                    y = self.dataset[y_axis_data]
                    xmin = st.number_input("Enter xmin for horizontal lines", value=0.0)
                    xmax = st.number_input("Enter xmax for horizontal lines", value=1.0)
                    plt.figure()
                    plt.hlines(y, xmin, xmax, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Filled Polygons Plot':
                    x = self.dataset[x_axis_data]
                    y = self.dataset[y_axis_data]
                    plt.figure()
                    plt.fill(x, y, color=color, alpha=alpha)
                    plt.title(title)
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    st.pyplot(plt.gcf())

                if plot_types=='Polar Plot':
                    theta = self.dataset[x_axis_data]
                    r = self.dataset[y_axis_data]
                    plt.figure()
                    plt.polar(theta, r, color=color, linestyle=linestyle, linewidth=linewidth, marker=marker, markersize=markersize, alpha=alpha)
                    plt.title(title)
                    st.pyplot(plt.gcf())

    def properties(self):
        # Input fields for common properties
        title = st.text_input("Title of the plot", "My Plot")
        xlabel = st.text_input("X-axis Label", "X-axis")
        ylabel = st.text_input("Y-axis Label", "Y-axis")
        alpha = st.slider("Select transparency (0.0 to 1.0)", 0.0, 1.0, 0.5)
        return title, xlabel, ylabel, alpha

    def plot(self):
        col1, col2 = st.columns([1,2])
    
    # List of available plot types
        available_plots = [
            'Line Plot', 'Error Bar Plot', 'Scatter Plot', 'Step Plot', 'Log-Log Plot', 
            'Semi-Log X Plot', 'Semi-Log Y Plot', 'Fill Between Plot', 'Fill Between X Plot', 
            'Bar Plot', 'Horizontal Bar Plot', 'Stem Plot', 'Event Plot', 'Pie Chart', 
            'Stacked Area Plot', 'Broken Barh Plot', 'Vertical Lines Plot', 'Horizontal Lines Plot', 
            'Filled Polygons Plot', 'Polar Plot'
        ]
    
        with col1:
        # Loop through the list and create checkboxes for each plot type
            for plot_type in available_plots:
                if st.checkbox(plot_type):
                # Pass the selected plot type to the allPlots method
                    self.allPlots(plot_type,col2)

class AllPlots:
    def __init__(self, dataset):
        self.dataset = dataset
        self.numerical_columns = self.dataset.select_dtypes(include=["int8","int16","float16", "int32", "int64", "float32", "float64"])
        self.categorical_columns = self.dataset.select_dtypes(include=["category", "string", "object"])

    def relplot(self):
        for i in range(len(self.numerical_columns.columns)):
            for j in range(i + 1, len(self.numerical_columns.columns)):
                x_col = self.numerical_columns.columns[i]
                y_col = self.numerical_columns.columns[j]
                
                # Scatterplot
                st.write(f"### Scatterplot: {x_col} vs {y_col}")
                plt.figure(figsize=(10, 6))
                sns.scatterplot(data=self.dataset, x=x_col, y=y_col)
                plt.title(f"{x_col} vs {y_col}")
                st.pyplot(plt)
                
                # Lineplot
                st.write(f"### Lineplot: {x_col} vs {y_col}")
                plt.figure(figsize=(10, 6))
                sns.lineplot(data=self.dataset, x=x_col, y=y_col)
                plt.title(f"{x_col} vs {y_col}")
                st.pyplot(plt)
                
                # Relplot (which can do both scatter and line plots via kind parameter)
                st.write(f"### Relplot: {x_col} vs {y_col}")
                plt.figure(figsize=(10, 6))
                sns.relplot(data=self.dataset, x=x_col, y=y_col, kind="scatter")
                plt.title(f"{x_col} vs {y_col} - Scatter")
                st.pyplot(plt)
                
                plt.figure(figsize=(10, 6))
                sns.relplot(data=self.dataset, x=x_col, y=y_col, kind="line")
                plt.title(f"{x_col} vs {y_col} - Line")
                st.pyplot(plt)
    
    def distributions(self):
        for i in range(len(self.numerical_columns.columns)):
            for j in range(i + 1, len(self.numerical_columns.columns)):
                x_col = self.numerical_columns.columns[i]
                y_col = self.numerical_columns.columns[j]
                
                # Histplot (Bivariate)
                st.write(f"### Histplot: {x_col} vs {y_col}")
                plt.figure(figsize=(10, 6))
                sns.histplot(data=self.dataset, x=x_col, y=y_col)
                plt.title(f"Histogram: {x_col} vs {y_col}")
                st.pyplot(plt)
                
                # KDEplot (Bivariate)
                st.write(f"### KDEplot: {x_col} vs {y_col}")
                plt.figure(figsize=(10, 6))
                sns.kdeplot(data=self.dataset, x=x_col, y=y_col)
                plt.title(f"KDE: {x_col} vs {y_col}")
                st.pyplot(plt)
                
                # ECDFplot (Univariate)
                st.write(f"### ECDFplot: {x_col}")
                plt.figure(figsize=(10, 6))
                sns.ecdfplot(data=self.dataset, x=x_col)
                plt.title(f"ECDF: {x_col}")
                st.pyplot(plt)

                st.write(f"### ECDFplot: {y_col}")
                plt.figure(figsize=(10, 6))
                sns.ecdfplot(data=self.dataset, x=y_col)
                plt.title(f"ECDF: {y_col}")
                st.pyplot(plt)
                
                # Rugplot
                st.write(f"### Rugplot: {x_col} vs {y_col}")
                plt.figure(figsize=(10, 6))
                sns.rugplot(data=self.dataset, x=x_col, y=y_col)
                plt.title(f"Rugplot: {x_col} vs {y_col}")
                st.pyplot(plt)

    def regression_plots(self):
        for i in range(len(self.numerical_columns.columns)):
            for j in range(i + 1, len(self.numerical_columns.columns)):
                x_col = self.numerical_columns.columns[i]
                y_col = self.numerical_columns.columns[j]
            
                # lmplot
                try:
                    st.write(f"### lmplot: {x_col} vs {y_col}")
                    sns.lmplot(data=self.dataset, x=x_col, y=y_col, height=6, aspect=1.5)
                    plt.title(f"Linear Regression Model: {x_col} vs {y_col}")
                    st.pyplot(plt)
                except:
                    st.info(f"SOME ERROR GENERATED WHEN GENEARTING LMPLOT FOR {x_col} VS {y_col}")

                # regplot
                try:
                    st.write(f"### regplot: {x_col} vs {y_col}")
                    plt.figure(figsize=(10, 6))
                    sns.regplot(data=self.dataset, x=x_col, y=y_col)
                    plt.title(f"Regression Plot: {x_col} vs {y_col}")
                    st.pyplot(plt)
                except:
                    st.info(f"SOME ERROR GENERATED WHEN GENEARTING REGPLOT FOR {x_col} VS {y_col}")
                
                # residplot
                try:
                    st.write(f"### residplot: Residuals of {x_col} vs {y_col}")
                    plt.figure(figsize=(10, 6))
                    sns.residplot(data=self.dataset, x=x_col, y=y_col)
                    plt.title(f"Residual Plot: {x_col} vs {y_col}")
                    st.pyplot(plt)
                except:
                    st.info(f"SOME ERROR GENERATED WHEN GENEARTING RESIDPLOT FOR {x_col} VS {y_col}")
                    
    def matrix_plots(self):
        for i in range(len(self.numerical_columns.columns)):
            for j in range(i + 1, len(self.numerical_columns.columns)):
                x_col = self.numerical_columns.columns[i]
                y_col = self.numerical_columns.columns[j]

            # Compute the correlation matrix for the selected pair of columns
                corr_matrix = self.dataset[[x_col, y_col]].corr()

            # Heatmap
                try:
                    st.write(f"### Heatmap: {x_col} vs {y_col}")
                    plt.figure(figsize=(8, 6))
                    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
                    plt.title(f"Heatmap of Correlation: {x_col} vs {y_col}")
                    st.pyplot(plt)
                except:
                    st.info()

            # Clustermap
                st.write(f"### Clustermap: {x_col} vs {y_col}")
                sns.clustermap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", figsize=(8, 6))
                plt.title(f"Clustermap of Correlation: {x_col} vs {y_col}")
                st.pyplot(plt)
    def multi_plot_grids(self):
    # Pairplot
        st.write("### Pairplot: Pairwise Relationships Between Numerical Variables")
        sns.pairplot(self.dataset[self.numerical_columns.columns])
        st.pyplot(plt)

    # PairGrid
        st.write("### PairGrid: Customized Pairwise Plots")
        pair_grid = sns.PairGrid(self.dataset[self.numerical_columns.columns])
        pair_grid.map_diag(sns.histplot)
        pair_grid.map_offdiag(sns.scatterplot)
        st.pyplot(pair_grid.fig)

    # Jointplot
        for i in range(len(self.numerical_columns.columns)):
            for j in range(i + 1, len(self.numerical_columns.columns)):
                x_col = self.numerical_columns.columns[i]
                y_col = self.numerical_columns.columns[j]

                st.write(f"### Jointplot: {x_col} vs {y_col}")
                sns.jointplot(data=self.dataset, x=x_col, y=y_col, kind="scatter", marginal_kws=dict(bins=15, fill=True))
                plt.title(f"Jointplot: {x_col} vs {y_col}", loc='left')
                st.pyplot(plt)

    # JointGrid
        for i in range(len(self.numerical_columns.columns)):
            for j in range(i + 1, len(self.numerical_columns.columns)):
                x_col = self.numerical_columns.columns[i]
                y_col = self.numerical_columns.columns[j]

                st.write(f"### JointGrid: Customized Jointplot for {x_col} vs {y_col}")
                joint_grid = sns.JointGrid(data=self.dataset, x=x_col, y=y_col)
                joint_grid.plot(sns.scatterplot, sns.histplot)
                st.pyplot(joint_grid.fig)
        st.divider()


class Cat_allPlots_num:
    def __init__(self, dataset):
        self.dataset = dataset
        self.numerical_columns = dataset.select_dtypes(include=["int8", "int32", "int64", "float32", "float64"])
        self.categorical_columns = dataset.select_dtypes(include=["category", "string", "object"]).copy()
        self.removed_columns = []

    def remove_high_cardinality_columns(self):
        """Removes categorical columns with more than 10 unique values."""
        for col in self.categorical_columns.columns:
            if self.categorical_columns[col].nunique() > 10:
                self.categorical_columns.drop(columns=col, inplace=True)
                self.removed_columns.append(col)

        if self.removed_columns:
            st.write(f"Dear user, we removed the following categorical columns from plotting due to their high cardinality: {self.removed_columns}")

    def relplot(self, hue):
        for i in range(len(self.numerical_columns.columns)):
            for j in range(i + 1, len(self.numerical_columns.columns)):
                x_col = self.numerical_columns.columns[i]
                y_col = self.numerical_columns.columns[j]

                # Scatterplot with Hue
                try:
                    st.write(f"### Scatterplot: {x_col} vs {y_col} (Categorical Hue: {hue})")
                    plt.figure(figsize=(10, 6))
                    sns.scatterplot(data=self.dataset, x=x_col, y=y_col, hue=hue)
                    plt.title(f"Scatterplot: {x_col} vs {y_col} with {hue} Hue")
                    st.pyplot(plt)
                except:
                    st.info(f"An error occurred when generating scatterplot for {x_col} vs {y_col} with {hue} Hue.")

                # Lineplot with Hue
                try:
                    st.write(f"### Lineplot: {x_col} vs {y_col} (Categorical Hue: {hue})")
                    plt.figure(figsize=(10, 6))
                    sns.lineplot(data=self.dataset, x=x_col, y=y_col, hue=hue)
                    plt.title(f"Lineplot: {x_col} vs {y_col} with {hue} Hue")
                    st.pyplot(plt)
                except:
                    st.info(f"An error occurred when generating lineplot for {x_col} vs {y_col} with {hue} Hue.")

    def main(self):
        self.remove_high_cardinality_columns()

        # Loop through each pair of categorical columns and call self.relplot() for each pair
        for col in self.categorical_columns.columns:
            for hue in self.categorical_columns.columns:
                if col != hue:
                    self.relplot(hue)

class Cat_Cat:
    def __init__(self, dataset):
        self.dataset = dataset
        self.categorical_columns = dataset.select_dtypes(include=["category", "string", "object"]).copy()
        self.removed_columns = []

    def remove_high_cardinality_columns(self):
        """Remove categorical columns with more than 10 unique values."""
        for col in self.categorical_columns.columns:
            if self.categorical_columns[col].nunique() > 10:
                self.categorical_columns.drop(columns=col, inplace=True)
                self.removed_columns.append(col)
        
        if self.removed_columns:
            st.write(f"Dear user, we removed the following categorical columns from plotting due to their high cardinality: {self.removed_columns}")

    def count_plot(self, col_x, col_y):
        st.write(f"### Count Plot: {col_x} vs {col_y}")
        sns.countplot(data=self.dataset, x=col_x, hue=col_y)
        st.pyplot(plt)
        plt.clf()

    def heatmap_plot(self, col_x, col_y):
        st.write(f"### Heatmap: {col_x} vs {col_y}")
        cross_tab = pd.crosstab(self.dataset[col_x], self.dataset[col_y])
        sns.heatmap(cross_tab, annot=True, fmt="d")
        st.pyplot(plt)
        plt.clf()

    def point_plot(self, col_x, col_y):
        st.write(f"### Point Plot: {col_x} vs {col_y}")
        sns.pointplot(data=self.dataset, x=col_x, y=col_y)
        st.pyplot(plt)
        plt.clf()

    def boxen_plot(self, col_x, col_y):
        st.write(f"### Boxen Plot: {col_x} vs {col_y}")
        sns.boxenplot(data=self.dataset, x=col_x, y=col_y)
        st.pyplot(plt)
        plt.clf()

    def strip_plot(self, col_x, col_y):
        st.write(f"### Strip Plot: {col_x} vs {col_y}")
        sns.stripplot(data=self.dataset, x=col_x, y=col_y)
        st.pyplot(plt)
        plt.clf()

    def violin_plot(self, col_x, col_y):
        st.write(f"### Violin Plot: {col_x} vs {col_y}")
        sns.violinplot(data=self.dataset, x=col_x, y=col_y)
        st.pyplot(plt)
        plt.clf()

    def swarm_plot(self, col_x, col_y):
        st.write(f"### Swarm Plot: {col_x} vs {col_y}")
        sns.swarmplot(data=self.dataset, x=col_x, y=col_y)
        st.pyplot(plt)
        plt.clf()

    def pairplot(self, col_x, col_y):
        st.write(f"### Pairplot: {col_x} vs {col_y}")
        sns.pairplot(self.dataset, hue=col_x)
        st.pyplot(plt)
        plt.clf()

    def main(self):
        self.remove_high_cardinality_columns()

        if len(self.categorical_columns.columns) == 0:
            st.write("No categorical columns available for plotting after filtering high cardinality columns.")
            return

        for i in range(len(self.categorical_columns.columns)):
            for j in range(i + 1, len(self.categorical_columns.columns)):
                col_x = self.categorical_columns.columns[i]
                col_y = self.categorical_columns.columns[j]
                
                self.count_plot(col_x, col_y)
                self.heatmap_plot(col_x, col_y)
                self.point_plot(col_x, col_y)
                self.boxen_plot(col_x, col_y)
                self.strip_plot(col_x, col_y)
                self.violin_plot(col_x, col_y)
                self.swarm_plot(col_x, col_y)
                self.pairplot(col_x, col_y)



                   
# Sidebar for file upload and menu
csv_file = st.sidebar.file_uploader("Upload Any CSV File", type=["csv"])
with st.sidebar:
    option_menus = option_menu("Analyser Menu", ["Pandas Basic Informative Dashboard",  "Univariate Analysis",
                                                     "Implement Seaborn Graphs", "Implement Matplotlib Graphs","Hundred's of plots"])

# Check if a CSV file is uploaded
if csv_file:
    # Reading the uploaded file as bytes (file-like object)
    csv_bytes = csv_file.read(100000)  # Read the first 100KB to detect encoding
    result = chardet.detect(csv_bytes)
    encoding = result['encoding']

    # Move back to the start of the file after reading
    csv_file.seek(0)

    # Read CSV using the detected encoding
    dataframe = pd.read_csv(csv_file, encoding=encoding)

    # Assuming `krishna` is an instance of a class that contains the method `data_cleaning`.
    value = krishna.data_cleaning(dataframe)

    # Option for Pandas Basic Informative Dashboard
    if option_menus == "Pandas Basic Informative Dashboard":
        pandas = Statistics(value)
        pandas.basic_details()
        pandas.secondary_information()
        pandas.statistics_1()
        pandas.statistics_2()

    # Option for Univariate Analysis
    elif option_menus == "Univariate Analysis":
        with st.expander("Univariate Analysis - Basic"):
            univariateAnalysis = UnivariateWithoutHue(value)
            cc, nc = univariateAnalysis.extract_columns()
            univariateAnalysis.layout(nc)

        with st.expander("Univariate Analysis - Intermediate"):
            uWh = UnivariateAnalysisWithHue(value)
            uWh.layout()

    # Option for Implementing Seaborn Graphs
    elif option_menus == "Implement Seaborn Graphs":
        with st.expander("Play with graphs and charts - 100% customizable"):
            displot = st.checkbox("Apply distribution plot")
            histplot = st.checkbox("Apply HistPlot")
            kdePlot = st.checkbox("Apply KDE Plot")
            ecdf = st.checkbox("Apply ECDF Plot")
            rugplot = st.checkbox("Apply RUG Plot")
            catplot = st.checkbox("Apply CAT Plot")
            stripplot = st.checkbox("Apply Stripplot")
            swarmplot = st.checkbox("Apply Swarm Plot")
            boxplot = st.checkbox("Apply Box Plot")
            violinplot = st.checkbox("Apply violin plot")
            boxenplot = st.checkbox("Apply Boxen plot")
            pointplot = st.checkbox("Apply Point Plot")
            barplot = st.checkbox("Apply Bar Plot")
            countplot = st.checkbox("Apply Count Plot")
            lmplot = st.checkbox("Apply Lmplot")
            regplot = st.checkbox("Apply Reg Plot")
            residplot = st.checkbox("Apply Resid Plot")
            heatmap = st.checkbox("Apply Heat Map")
            jointplot = st.checkbox("Apply Joint Plot")
            pairplot = st.checkbox("Apply Pair Plot")

            # Plotting based on user selection
            if displot:
                Displot(value).plot()
            if histplot:
                Histplot(value).plot()  # Corrected to match the class name casing
            if kdePlot:
                Kdeplot(value).plot()
            if ecdf:
                Ecdfplot(value).plot()
            if rugplot:
                Rugplot(value).plot()
            if catplot:
                Catplot(value).plot()
            if stripplot:
                Stripplot(value).plot()
            if swarmplot:
                Swarmplot(value).plot()
            if boxplot:
                Boxplot(value).plot()
            if violinplot:
                Violinplot(value).plot()
            if boxenplot:
                Boxenplot(value).plot()
            if pointplot:
                Pointplot(value).plot()
            if barplot:
                Barplot(value).plot()
            if countplot:
                Countplot(value).plot()
            if lmplot:
                Lmplot(value).plot()
            if regplot:
                Regplot(value).plot()
            if residplot:
                Residplot(value).plot()
            if heatmap:
                Heatmap(value).plot()
            if jointplot:
                Jointplot(value).plot()
            if pairplot:
                Pairplot(value).plot()
    elif option_menus=="Implement Matplotlib Graphs":
        Matplotlib(value).plot()
    elif option_menus=="AutoML":
        PyCaretML(dataframe).regressor()
    elif option_menus == "Hundred's of plots":
        all_plots_instance = AllPlots(value)
        col1,col2=st.columns([1,2])
        with col1:
            if st.checkbox("Apply ALL Rel Plots"):
                with col2:
                    all_plots_instance.relplot()
            if st.checkbox("Apply ALL Distribution Plots"):
                with col2:
                    all_plots_instance.distributions()
            if st.checkbox("Apply ALL Regression Plots"):
                with col2:
                    all_plots_instance.regression_plots()
            if st.checkbox("Apply ALL Matrix Plots"):
                with col2:
                    all_plots_instance.matrix_plots()
            if st.checkbox("Apply ALL Multi Plot grids"):
                with col2:
                    all_plots_instance.multi_plot_grids()
            if st.checkbox("Apply ALL Categorical Plots"):
                with col2:
                    cat_plots_instance = Cat_allPlots_num(value)
                    cat_plots_instance.main()
            if st.checkbox("Apply ALL Categorical Plots VS CAtegorical Plots"):
                with col2:
                    Cat_Cat(value).main()
