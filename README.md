haldataset:
https://contestfiles.storage.yandexcloud.net/companies/76b19c3f3c417fc4f9623ba4d00cbde8/train.csv?roistat_visit=1415538



def draw_graph(buyeruid):
    print(buyeruid)
    #ons = oneclientline_df.iloc[loi]
    ons = oneclientline_df[oneclientline_df['buyeruid'] == buyeruid].iloc[0]
    dayslist = list(range(1,29))
    fig, ax = plt.subplots() #figsize=(3, 3))
    fig.set_size_inches(4, 2)
    plt.ylim (1, 100)
    plt.xlim (0.5, 28.5)
    for i in range(28): #Пытаемся менять цвета
        #ax.fill_between(dayslist[i:i+2], 0, ons.days_array[i:i+2],
        ax.fill_between([dayslist[i:i+1][0]-0.5, dayslist[i:i+1][0]+0.5 ], 0, ons.days_array[i:i+1]*2,
                    #facecolor='#{:02X}{:02X}{:02X}'.format(255-ons.days_array[i:i+2][0]*2, 10+ons.days_array[i:i+2][0]*2, 0),
                    #color = '#{:02X}{:02X}{:02X}'.format(255-ons.days_array[i:i+2][0]*2, 10+ons.days_array[i:i+2][0]*2, 0),    #  цвет линий
                    facecolor='#{:02X}{:02X}{:02X}'.format(255-ons.days_array[i:i+1][0]*2, 10+ons.days_array[i:i+1][0]*2, 0),
                    color = '#{:02X}{:02X}{:02X}'.format(255-ons.days_array[i:i+1][0]*2, 10+ons.days_array[i:i+1][0]*2, 0),    #  цвет линий
                    alpha = 0.5,
                    linewidth = 1,      #  ширина линий
                    linestyle = '--')   #  начертание линий
        #fig.set_figwidth(12)    #  ширина и
        #fig.set_figheight(6)    #  высота "Figure"
        fig.set_facecolor('white') #'white')
        ax.set_facecolor('#{:02X}{:02X}{:02X}'.format(250, 250, 250)) #'white')
    plt.xlabel("дни месяца", fontsize=8) #, fontweight="bold")
    plt.ylabel("верятность покупки", fontsize=8) #, fontweight="bold")
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_major_locator(plt.FixedLocator([1, 10, 20, 28]))
    ax.yaxis.set_major_locator(plt.FixedLocator(list(range(0,101,5))  ))
    ax.yaxis.set_major_formatter(plt.FixedFormatter( [ jo if jo in [0, 25, 50, 75, 100] else '' for jo in list(range(0,101,5))]    ))
    plt.show()
    
for loi in [28, 72,85,2]:
    draw_graph(oneclientline_df.iloc[loi].buyeruid)
    
for loi in ['3a599c56-fec9-11e8-80d0-0cc47aabb0b2',
            '54d5abf0-45f4-11eb-811c-0cc47aabb0b2',
            'f6ae5374-1ad9-11ec-8123-0cc47aabb0b2',
            '0b046315-54fb-11e7-80c8-0cc47aabb0b2',
            'b6a82b5a-54fa-11e7-80c8-0cc47aabb0b2',
            '35e06b19-1363-11e6-b53d-001d72335c95',
            '120986b9-1bc8-11e8-80c9-0cc47aabb0b2']:
    draw_graph(loi)
