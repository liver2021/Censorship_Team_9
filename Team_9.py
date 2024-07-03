import matplotlib.pyplot as plt 

def NaN_Plot(df,country,year):
    categories = ['http-failure', 'http-diff', 'dns', 'tcp_ip']
    for category in categories:
        df[category] = df['blocking_type'] == category
        df['NaN'] = df['blocking_type'].isna()
    Blockings_df = df.groupby(['year', 'month']).agg(
    http_count=('http-failure', lambda x: (x == True).sum()),
    http_diff_count=('http-diff', lambda x: (x == True).sum()),
    dns_count=('dns', lambda x: (x == True).sum()),
    tcp_ip_count=('tcp_ip', lambda x: (x == True).sum()),NaN_count=('NaN', lambda x: (x == True).sum())).reset_index()
    fig = plt.figure(figsize = (10, 5))
    x = Blockings_df['month']
    y = Blockings_df['NaN_count']
    plt.bar(x, y, color ='maroon', 
        width = 0.4)
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.title(f"NaN Values for Blocking for {country} in {str(year)}")
    
    file_path = f"OONI_Project/NaN_{country}_{year}.png"
    plt.savefig(file_path,transparent=True)

def blocking(df, country,year):
    categories = ['http-failure', 'http-diff', 'dns', 'tcp_ip']
    for category in categories:
        df[category] = df['blocking_type'] == category
        df['NaN'] = df['blocking_type'].isna()
    Blockings_df = df.groupby(['year', 'month']).agg(
    http_count=('http-failure', lambda x: (x == True).sum()),
    http_diff_count=('http-diff', lambda x: (x == True).sum()),
    dns_count=('dns', lambda x: (x == True).sum()),
    tcp_ip_count=('tcp_ip', lambda x: (x == True).sum()),
    NaN_count=('NaN', lambda x: (x == True).sum())).reset_index()
        

    months = Blockings_df['month']
    plt.figure(figsize=(12, 8))
    plt.suptitle(f'Blocking Types Count by Month for {country} in {str(year)} ', fontsize=16)

    plt.subplot(221)  
    plt.bar(months, Blockings_df['http_count'], color='blue')
    plt.title('HTTP')
    plt.xlabel('Month')
    plt.ylabel('Count')

    plt.subplot(222)  
    plt.bar(months, Blockings_df['http_diff_count'], color='green')
    plt.title('HTTP Diff')
    plt.xlabel('Month')
    plt.ylabel('Count')

    plt.subplot(223)  
    plt.bar(months, Blockings_df['dns_count'], color='red')
    plt.title('DNS')
    plt.xlabel('Month')
    plt.ylabel('Count')

    plt.subplot(224)  
    plt.bar(months, Blockings_df['tcp_ip_count'], color='purple')
    plt.title('TCP/IP')
    plt.xlabel('Month')
    plt.ylabel('Count')
        
    plt.tight_layout()
    file_path = f"OONI_Project/block_{country}_{year}.png"
    file_path_1 = f"OONI_Project/block_{country}_{year}.csv"

    plt.savefig(file_path,transparent=True)
    Blockings_df.to_csv(file_path_1, index=False)  

    return Blockings_df



def do_plots(df,country,year):

    grouped_df = df.groupby(['year', 'month']).agg(
    anomaly_count=('anomaly', lambda x: (x == True).sum()),
    confirmed_count=('confirmed', lambda x: (x == True).sum()),
    failure_count=('failure', lambda x: (x == True).sum()),
    valid_count=('valid', lambda x: (x == True).sum())).reset_index()
    
    months = grouped_df['month']
    plt.figure(figsize=(12, 8))
    plt.suptitle(f'Evidence for Censorship in {country} {str(year)} ', fontsize=16)
    plt.subplot(221)  
    plt.bar(months, grouped_df['anomaly_count'], color='blue')
    plt.title('Anomaly')
    plt.xlabel('Month')
    plt.ylabel('Count')

    plt.subplot(222)  
    plt.bar(months, grouped_df['confirmed_count'], color='green')
    plt.title('Confirmed')
    plt.xlabel('Month')
    plt.ylabel('Count')

    plt.subplot(223)  
    plt.bar(months, grouped_df['failure_count'], color='red')
    plt.title('Failure')
    plt.xlabel('Month')
    plt.ylabel('Count')

    plt.subplot(224)  
    plt.bar(months, grouped_df['valid_count'], color='purple')
    plt.title('Valid')
    plt.xlabel('Month')
    plt.ylabel('Count')
    
    plt.tight_layout()
    country = country
    file_path = f"OONI_Project/{country}_{year}.png"
    file_path_1 = f"OONI_Project/{country}_{year}.csv"
    plt.savefig(file_path,transparent=True)
    grouped_df.to_csv(file_path_1, index=False)  

    return grouped_df
        


    
        

 
