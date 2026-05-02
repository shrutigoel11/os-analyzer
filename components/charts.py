import plotly.express as px

def plot_bar(df, column, title):
    fig = px.bar(
        df.groupby("OS")[column].mean().reset_index(),
        x="OS",
        y=column,
        color="OS",
        title=title
    )
    return fig