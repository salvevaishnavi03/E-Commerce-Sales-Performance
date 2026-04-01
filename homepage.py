import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.markdown(
    """
    <div style="
        background-color:#8B4513;
        padding:18px;
        border-radius:10px;
        text-align:center;
    ">
        <h1 style="
            color:white;
            margin:0;
        ">
            🛒 E-Commerce Sales Performance Dashboard
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)




# ---------------- LOAD DATA ----------------
df = pd.read_excel("project Data new.xlsx")

# ---------------- SIDEBAR FILTER ----------------

st.sidebar.image("cyber-monday-shopping-sales.jpg", width=300)

st.sidebar.header("Filter Data")


gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

occupation_filter = st.sidebar.multiselect(
    "Select Occupation",
    options=df["Occupation"].unique(),
    default=df["Occupation"].unique()
)

filtered_df = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Occupation"].isin(occupation_filter))
]



#----------about dashboard-------------

st.markdown(
    """
    <div style="
        background-color:#F0D7CA;
        padding:25px;
        border-radius:12px;
        border-left:6px solid #8B4513;
        margin-top:10px;
    ">

    <h3 style="color:#8B4513;">📊 About This Dashboard</h3>

    <p style="font-size:16px; line-height:1.6;">
    This E-Commerce Sales Performance Dashboard provides insights into customer purchasing behavior
    and overall sales performance. The dashboard highlights key business metrics such as total sales,
    total customers, and average order value to help understand revenue trends.
    </p>

    <p style="font-size:16px; line-height:1.6;">
    Interactive filters in the sidebar allow users to analyze sales based on gender and occupation,
    making it easier to identify customer segments contributing the most to revenue.
    Visualizations such as gender-based sales distribution and the top five customers chart
    help in quickly understanding patterns and identifying high-value customers.
    </p>

    <p style="font-size:16px; line-height:1.6;">
    Overall, this dashboard helps businesses monitor performance, explore customer demographics,
    and make data-driven decisions to improve marketing strategies and sales growth.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

#-----------------------------------

# ---------------- KPI CARDS ----------------
total_sales = filtered_df["Amount"].sum()
total_customers = filtered_df["Cust_name"].nunique()
avg_order = filtered_df["Amount"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"₹ {total_sales:,.0f}")
col2.metric("👥 Total Customers", total_customers)
col3.metric("🛒 Avg Order Value", f"₹ {avg_order:,.0f}")

st.divider()

# ---------------- TWO CHARTS SIDE BY SIDE ----------------

col1, col2 = st.columns([1,1]) 

# -------- PIE CHART --------
with col1:
    st.subheader("Amount Distribution by Gender")

    gender_data = filtered_df.groupby("Gender")["Amount"].sum()

    plt.figure(figsize=(4,4))
    color = ["#E2561F","#DF7040"]
    A=sns.countplot(x="Gender",data=df,hue="Marital_Status",palette=color,edgecolor="black",)

    plt.title("gender wise amount ",family="georgia",fontsize=16,fontweight="bold")
    plt.xlabel("")
    plt.ylabel("")
    st.pyplot(plt, use_container_width=True)
    plt.clf()


# -------- TOP 5 CUSTOMERS BAR CHART --------
with col2:
    st.subheader("Top 5 Customers")
    
    color_1 = [ "#E2561F", "#DF7040", "#E29D75", "#E2B194", "#F0D7CA"]

    top5 = (
        filtered_df.groupby("Cust_name")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(4,4))
    plt.bar(top5.index, top5.values, color=color_1)

    plt.xticks(rotation=45)
    plt.ylabel("Total Purchase Amount")

    st.pyplot(plt, use_container_width=True)
    plt.clf()

st.divider()

#------------description of both charts ---------------------------

col3, col4 = st.columns(2)

# -------- DESCRIPTION FOR GENDER CHART --------
with col3:
    st.markdown(
        """
        <div style="
            background-color:#F5E6DC;
            padding:18px;
            border-radius:10px;
            border-left:5px solid #E2561F;
        ">
        <h4 style="color:#8B4513;">📊 Amount Distribution by Gender</h4>

        <p style="font-size:15px; line-height:1.6;">
        This chart shows how the total purchase amount is distributed
        between male and female customers. It helps identify which
        gender contributes more to the overall revenue of the business.
        </p>

        <p style="font-size:15px; line-height:1.6;">
        By analyzing this distribution, businesses can better understand
        customer demographics and adjust marketing strategies to target
        the most valuable customer groups.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# -------- DESCRIPTION FOR TOP 5 CUSTOMERS --------
with col4:
    st.markdown(
        """
        <div style="
            background-color:#F5E6DC;
            padding:18px;
            border-radius:10px;
            border-left:5px solid #E2561F;
        ">
        <h4 style="color:#8B4513;">🏆 Top 5 Customers</h4>

        <p style="font-size:15px; line-height:1.6;">
        This chart highlights the top five customers who have contributed
        the highest purchase amounts. These customers play a key role in
        generating revenue for the business.
        </p>

        <p style="font-size:15px; line-height:1.6;">
        Identifying high-value customers helps businesses focus on
        customer retention strategies, personalized marketing,
        and loyalty programs to maintain long-term relationships.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
#----------------------end of description-------------------


st.subheader("occupation wise Amount")
    
plt.figure(figsize=(15,4))
sns.lineplot(x="Occupation",y="Amount",errorbar=None,data=df,marker="o",color="#CA6721")
plt.xticks(rotation=90)

plt.xlabel("")
plt.ylabel("")  
plt.grid(color="#93654A")
plt.show()
    
    
st.pyplot(plt, use_container_width=True)
plt.clf()

st.divider()

#-------------description of linechart------------------------

st.markdown(
    """
    <div style="
        background-color:#F5E6DC;
        padding:20px;
        border-radius:10px;
        border-left:6px solid #CA6721;
        margin-top:10px;
    ">
    
    <h4 style="color:#8B4513;">📈 Occupation-wise Sales Analysis</h4>

    <p style="font-size:15px; line-height:1.6;">
    This line chart represents the total purchase amount contributed by customers
    from different occupations. It helps analyze which professional groups are
    spending more on the platform and contributing significantly to overall revenue.
    </p>

    <p style="font-size:15px; line-height:1.6;">
    By studying this trend, businesses can identify high-value occupational segments
    and design targeted marketing campaigns, promotions, or product offerings that
    appeal to these customer groups.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()
#------------end of description of line chart--------------------------

#-------------countplot
col3, col4 = st.columns([1,1])

# -------- CHART --------
with col3:

    st.subheader("Age Wise Count")

    plt.figure(figsize=(4,4))

    color = [ "#E2561F", "#DF7040", "#E29D75", "#E2B194", "#F0D7CA"]

    sns.countplot(
        x="Age Group",
        data=df,
        hue="Zone",
        palette=color,
        edgecolor="black"
    )

    plt.xlabel("")
    plt.ylabel("")
    plt.xticks(rotation=45)

    st.pyplot(plt, use_container_width=True)
    plt.clf()


# -------- DESCRIPTION BOX --------
with col4:

    st.markdown(
        """
        <div style="
            background-color:#F5E6DC;
            padding:20px;
            border-radius:10px;
            border-left:6px solid #E2561F;
        ">

        <h4 style="color:#8B4513;">👥 Age Group Customer Distribution</h4>

        <p style="font-size:15px; line-height:1.6;">
        This chart represents the distribution of customers across
        different age groups along with their regional zones.
        It helps identify which age segments are more active
        in purchasing products.
        </p>

        <p style="font-size:15px; line-height:1.6;">
        By analyzing this information, businesses can better
        understand customer demographics and focus marketing
        strategies on the most active age groups and regions.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()