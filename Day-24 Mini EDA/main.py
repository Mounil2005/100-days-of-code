import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="CSV QuickLook", layout="wide")

st.title("📊 CSV QuickLook — Mini EDA")
st.write("Upload a CSV to explore columns, missing values, stats, and quick charts.")

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded is None:
    st.info("Tip: Try with a sample dataset like Titanic or Iris.")
    st.stop()


@st.cache_data
def load_df(file):
    return pd.read_csv(file)

try:
    df = load_df(uploaded)
except Exception as e:
    st.error(f"Failed to read CSV: {e}")
    st.stop()

st.success(f"Loaded shape: {df.shape[0]} rows × {df.shape[1]} columns")


st.sidebar.header("🧹 Cleaning (optional)")
drop_dupes = st.sidebar.checkbox("Drop duplicate rows", value=True)
fillna_mode = st.sidebar.selectbox("Fill missing values with", ["Do nothing", "Zero (numeric only)", "Empty string (object only)"])

df_clean = df.copy()
if drop_dupes:
    before = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    after = len(df_clean)
    st.sidebar.caption(f"Removed {before - after} duplicate rows.")

if fillna_mode == "Zero (numeric only)":
    num_cols = df_clean.select_dtypes(include=["number"]).columns
    df_clean[num_cols] = df_clean[num_cols].fillna(0)
elif fillna_mode == "Empty string (object only)":
    obj_cols = df_clean.select_dtypes(include=["object", "string"]).columns
    df_clean[obj_cols] = df_clean[obj_cols].fillna("")


tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Missing Values", "Stats", "Charts"])

with tab1:
    st.subheader("Peek")
    n = st.slider("Rows to preview", 5, 50, 10, step=5)
    st.dataframe(df_clean.head(n), use_container_width=True)

    st.subheader("Schema")
    schema = pd.DataFrame({
        "column": df_clean.columns,
        "dtype": df_clean.dtypes.astype(str),
        "non_null": df_clean.notna().sum().values,
        "nulls": df_clean.isna().sum().values,
        "unique": df_clean.nunique().values
    })
    st.dataframe(schema, use_container_width=True)

with tab2:
    st.subheader("Missing Value Report")
    null_counts = df_clean.isna().sum().sort_values(ascending=False)
    if null_counts.sum() == 0:
        st.success("No missing values found 🎉")
    else:
        st.write(null_counts.to_frame("missing").T if len(null_counts) <= 12 else null_counts)
        # Bar chart
        fig, ax = plt.subplots()
        to_plot = null_counts[null_counts > 0]
        ax.bar(to_plot.index.astype(str), to_plot.values)
        ax.set_xticklabels(to_plot.index.astype(str), rotation=45, ha="right")
        ax.set_ylabel("Missing count")
        ax.set_title("Missing values per column")
        st.pyplot(fig, use_container_width=True)

with tab3:
    st.subheader("Numeric Summary")
    num_df = df_clean.select_dtypes(include=["number"])
    if num_df.empty:
        st.info("No numeric columns to summarize.")
    else:
        st.dataframe(num_df.describe().T, use_container_width=True)

with tab4:
    st.subheader("Quick Charts")
    st.caption("Create a histogram or scatter plot from your columns.")

    
    st.markdown("**Histogram**")
    hist_col = st.selectbox("Select a column", df_clean.columns, key="hist")
    if hist_col:
        if pd.api.types.is_numeric_dtype(df_clean[hist_col]):
            values = df_clean[hist_col].dropna().values
            fig, ax = plt.subplots()
            ax.hist(values, bins=30)
            ax.set_title(f"Histogram — {hist_col}")
            ax.set_xlabel(hist_col)
            ax.set_ylabel("Frequency")
            st.pyplot(fig, use_container_width=True)
        else:
            st.info("Selected column is non‑numeric. Showing top categories instead.")
            counts = df_clean[hist_col].astype(str).value_counts().head(20)
            fig, ax = plt.subplots()
            ax.bar(counts.index, counts.values)
            ax.set_xticklabels(counts.index, rotation=45, ha="right")
            ax.set_title(f"Top categories — {hist_col}")
            ax.set_ylabel("Count")
            st.pyplot(fig, use_container_width=True)

    st.divider()

    
    num_cols = df_clean.select_dtypes(include=["number"]).columns.tolist()
    st.markdown("**Scatter Plot**")
    if len(num_cols) < 2:
        st.info("Need at least two numeric columns for scatter.")
    else:
        xcol = st.selectbox("X", num_cols, key="x")
        ycol = st.selectbox("Y", num_cols, key="y")
        if xcol and ycol and xcol != ycol:
            fig, ax = plt.subplots()
            ax.scatter(df_clean[xcol], df_clean[ycol], alpha=0.6)
            ax.set_xlabel(xcol)
            ax.set_ylabel(ycol)
            ax.set_title(f"{ycol} vs {xcol}")
            st.pyplot(fig, use_container_width=True)


buf = io.StringIO()
df_clean.to_csv(buf, index=False)
st.download_button("⬇️ Download cleaned CSV", data=buf.getvalue(), file_name="cleaned.csv", mime="text/csv")
