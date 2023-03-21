import pandas as pd
PATH = "//Users/junyuwu/Chipotle Project/components/chipotle.csv"
df = pd.read_csv(PATH)
df["ip"] = df["item_price"].str.split("$").apply(lambda x : x[1]).astype(float)

def get_revenue():
    top_rev = df.groupby("item_name")["ip"].sum().to_frame().sort_values("ip",ascending=False)[:5]
    top_rev.reset_index(inplace=True)
    top_rev.rename(columns = {'item_name': 'item'}, inplace=True)
    return top_rev

def get_revenue_list():
    top_rev = df.groupby("item_name")[["ip"]].sum()
    top_rev_df = top_rev.sort_values("ip",ascending=False).iloc[:5]
    top_rev_df_list = sorted(list(set(top_rev_df.index.tolist())))
    return top_rev_df_list

def get_quantity_list():
    top_quantity = df.groupby("item_name")["quantity"].sum().sort_values(ascending=False).to_frame()[:5]
    top_quantity_list = sorted(list(set(top_quantity.index.tolist())))
    return top_quantity_list

def get_quantity():
    top_quantity = df.groupby("item_name")["quantity"].sum().sort_values(ascending=False).to_frame()[:5]
    top_quantity.reset_index(inplace=True)
    top_quantity.rename(columns = {'item_name': 'item'}, inplace=True)
    return top_quantity