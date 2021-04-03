import billboard
import pandas as pd
import datetime

def hot_100_data(year_start, year_end):
    # haha you think I'd be responsible and add a docstring? LOSER!
    # TODO: change this
    
    all_hot_100 = pd.DataFrame(columns=["Date", "Song"])

    for year in range(year_start, year_end, 1):

        for month in [i + 1  for i in range(12)]:
            current_date = datetime.date(year, month, 1)
            current_chart = \
            billboard.ChartData("hot-100", date=current_date).entries
            for song in current_chart:
                all_hot_100 = all_hot_100.append({"Date": current_date, "Song": f"{song.title} {song.artist}"}, ignore_index=True)
        
    return all_hot_100
    


def convert_chart(current_chart):
    chart_list = []
    for chart_entry in current_chart:
        chart_list.append({"title": chart_entry.title, "artist": chart_entry.artist})
    return chart_list