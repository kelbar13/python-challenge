# Heroes of Pymoli Data Analysis
# Observed trend 1: Males make up the majority of players
# Observed trend 2: The majority of players are between the ages of 20 to 24
# Observed trend 3: Price is not a significant factor in purchases

```python
# Dependencies
import pandas as pd
import numpy as np
from collections import OrderedDict
```


```python
# Read json file
heroes = "purchase_data.json"
heroes_df = pd.read_json(heroes)
heroes_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Total count of players
total_players = len(heroes_df)
total_players
```




    780




```python
# Purchasing Analysis
# Number of unique items, average purchase price, total number of purchases, total revenue
unique_items = heroes_df["Item Name"].nunique()
avg_purchase = round(heroes_df["Price"].mean(),2)
total_purch = heroes_df["Price"].count()
total_revenue = round(heroes_df["Price"].sum(),2)

# Create new dataframe
purch_analysis = pd.DataFrame(OrderedDict({"Unique Items":[unique_items], 
                               "Avg Purchase Price":"$"+str(avg_purchase), 
                               "Total Purchases":[total_purch], 
                               "Total Revenue":"$"+str(total_revenue)}))
purch_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unique Items</th>
      <th>Avg Purchase Price</th>
      <th>Total Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Group data by gender
gender_group = heroes_df.groupby(["Gender"])
print(gender_group)
gender_group.count().head()
```

    <pandas.core.groupby.DataFrameGroupBy object at 0x00000221D6710D30>
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>136</td>
      <td>136</td>
      <td>136</td>
      <td>136</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>633</td>
      <td>633</td>
      <td>633</td>
      <td>633</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Percentage and Count of Male Players, Percentage and Count of Female Players, Percentage and Count of Other / Non-Disclosed
gender_count = heroes_df["Gender"].value_counts()
gender_percent = round(gender_count / total_players * 100, 2)

# Create dataframe
gender_analysis = pd.DataFrame({"Percentage of Players":gender_percent,
                                           "Total Count":gender_count})
gender_analysis.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.44</td>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.41</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchase Count, Average Purchase Price, Total Purchase Value, Normalized Totals by gender
avg_price = round(gender_group["Price"].mean(), 2)
total_value = round(gender_group['Price'].sum(), 2)
price_std = gender_group["Price"].std(ddof=0)
normal_total = round(avg_price/price_std, 2)
# Create dataframe
purch_analysis = pd.DataFrame(OrderedDict({"Purchase Count":gender_count,
                              "Average Purchase Price":"$" + avg_price.astype(str),
                              "Total Purchase Value":"$" + total_value.astype(str),
                              "Normalized Totals by Gender":"$" + normal_total.astype(str)}))
purch_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals by Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$2.46</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1867.68</td>
      <td>$2.66</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$3.56</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Age demographics find min/max for binning
print(heroes_df["Age"].max())
print(heroes_df["Age"].min())                                 
```

    45
    7
    


```python
# Create bins
bins = [0,10,15,20,25,30,35,40,50]
group_labels = ["<10","10 to 14","15 to 19","20 to 24","25 to 29","30 to 34","35 to 39","40+"]

# Slice the data and put it into bins
pd.cut(heroes_df["Age"],bins,labels=group_labels).head()
```




    0    35 to 39
    1    20 to 24
    2    30 to 34
    3    20 to 24
    4    20 to 24
    Name: Age, dtype: category
    Categories (8, object): [<10 < 10 to 14 < 15 to 19 < 20 to 24 < 25 to 29 < 30 to 34 < 35 to 39 < 40+]




```python
heroes_df["Age Group"] = pd.cut(heroes_df["Age"],bins,labels=group_labels)
heroes_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35 to 39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20 to 24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30 to 34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20 to 24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20 to 24</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Group by age group
age_group = heroes_df.groupby("Age Group")

# Break out Purchase Count, Average Purchase Price, Total Purchase Value, and Normalized Totals into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
purch_count = age_group["Price"].count() 
avg_price = round(age_group["Price"].mean(), 2)
total_value = round(age_group["Price"].sum(), 2)
price_std = age_group["Price"].std()
normal_total = round(avg_price/price_std, 2)

# Create dataframe
age_analysis = pd.DataFrame(OrderedDict({"Purchase Count":purch_count,
                                        "Average Purchase Price":"$" + avg_price.astype(str),
                                        "Total Purchase Value":"$" + total_value.astype(str),
                                        "Normalized Totals":"$" + normal_total.astype(str)}))
age_analysis

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$2.61</td>
    </tr>
    <tr>
      <th>10 to 14</th>
      <td>78</td>
      <td>$2.87</td>
      <td>$224.15</td>
      <td>$2.59</td>
    </tr>
    <tr>
      <th>15 to 19</th>
      <td>184</td>
      <td>$2.87</td>
      <td>$528.74</td>
      <td>$2.52</td>
    </tr>
    <tr>
      <th>20 to 24</th>
      <td>305</td>
      <td>$2.96</td>
      <td>$902.61</td>
      <td>$2.64</td>
    </tr>
    <tr>
      <th>25 to 29</th>
      <td>76</td>
      <td>$2.89</td>
      <td>$219.82</td>
      <td>$2.59</td>
    </tr>
    <tr>
      <th>30 to 34</th>
      <td>58</td>
      <td>$3.07</td>
      <td>$178.26</td>
      <td>$2.87</td>
    </tr>
    <tr>
      <th>35 to 39</th>
      <td>44</td>
      <td>$2.9</td>
      <td>$127.49</td>
      <td>$2.62</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
      <td>$3.34</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
# SN, Purchase Count, Average Purchase Price, Total Purchase Value
# Group by SN
sn_group = heroes_df.groupby("SN")

# Identify Purchase Count, Average Purchase Price, Total Purchase Value
purchase_count = sn_group["SN"].count()
avg_price = round(sn_group["Price"].mean(),2)
total_value = sn_group["Price"].sum()

# Create dataframe
spenders = pd.DataFrame(OrderedDict({"Purchase Count":purchase_count.astype(int),
                                        "Average Purchase Price":avg_price.astype(float),
                                        "Total Purchase Value":total_value.astype(float)}))
# Format column data -- did not return highest value
#spenders["Purchase Count"] = spenders["Purchase Count"].map("{:,}".format)
#spenders["Average Purchase Price"] = spenders["Average Purchase Price"].map("${:.2f}".format)
#spenders["Total Purchase Value"] = spenders["Total Purchase Value"].map("${:.2f}".format)

# Sort values to find top 5
top_spenders = spenders.sort_values(["Total Purchase Value"], ascending=False)
top_spenders.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>3.41</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>3.39</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>3.18</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>4.24</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>3.86</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Identify the 5 most popular items by purchase count, then list (in a table):
# Item ID, Item Name, Purchase Count, Item Price, Total Purchase Value
# Group by Item ID and Item Name
item_group = heroes_df.groupby(["Item ID","Item Name"])

# Identify Purchase Count, Item Price, Total Purchase Value
purch_count = item_group["Item ID"].count()
item_price = round(item_group["Price"].mean(),2)
total_value = round(item_group["Price"].sum(),2)

# Create dataframe
item_df = pd.DataFrame(OrderedDict({"Purchase Count":purch_count.astype(int),
                                      "Item Price":item_price.astype(float),
                                      "Total Purchase Value":total_value.astype(float)}))


# Format columns using .map -- did not return highest value
#item_df["Purchase Count"] = item_df["Purchase Count"].map("{:,}".format)
#item_df["Item Price"] = item_df["Item Price"].map("${:.2f}".format)
#item_df["Total Purchase Value"] = item_df["Total Purchase Value"].map("${:.2f}".format)

# Create sorted dataframe by purchase count
top_items = item_df.sort_values(["Purchase Count"], ascending=False)
top_items.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Identify the 5 most profitable items by total purchase value, then list (in a table):
# Item ID, Item Name, Purchase Count, Item Price, Total Purchase Value
# Create new dataframe to sort values in item_df by total purchase value
top_profit = item_df.sort_values(["Total Purchase Value"], ascending=0)
top_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


