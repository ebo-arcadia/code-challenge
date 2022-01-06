# Aim: Track the movement of three gulls namely – Eric, Nico & Sanne
# Dataset: official_datasets; used dataset – csv
# Dependencies: Matplotlib, Pandas, Numpy, Cartopy, Shapely
# Repository(Github): source code
# (check the repository for the documentation of source code.)
# Writeup: explanation(.pdf)

# We will divide our case study into five parts:
# 1. Visualizing longitude and latitude data of the gulls.
# 2. Visualize the variation of the speed of the gulls.
# 3. Visualize the time required by the gulls to cover equal distances over the journey.
# 4. Visualize the daily mean speed of the gulls.
# 5. Cartographic view of the journey of the gulls.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# PART (1/5): Latitude and Longitude

birddata = pd.read_csv("../python-mini-apps-file/bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

# storing the indices of the bird Eric
ix = birddata.bird_name == "Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize=(7, 7))
plt.plot(x, y, "b.")

''' To look at all the birds trajectories,
    we plot each bird in the same plot '''
plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    # storing the indices of the bird Eric
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()

# PART (2/5): 2D Speed Vs Frequency
# In this second part of the case study, we are going to visualize 2D speed vs Frequency for the gull named “Eric”.

birddata = pd.read_csv("../python-mini-apps-file/bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

# storing the indices of the bird Eric
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]

plt.figure(figsize=(8, 4))
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20))
plt.xlabel(" 2D speed (m/s) ")
plt.ylabel(" Frequency ")
plt.show()

# PART (3/5): Time and Date The third part is associated with date and time. We are going to visualize the time(in
# days) required by Eric to cover constant distances through his journey. If he covers equal distances in an equal
# amount of time, then the Elapsed time vs Observation curve will be linear.

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamp"] = pd.Series(timestamps, index=birddata.index)

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]

elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)


# PART (4/5): Daily Mean Speed We are going to visualize the daily mean speed of the gull named “Eric” for the total
# number of days of recorded flight.

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

# PART (5/5): Cartographic View
# In this last part, we are going to track the Birds over a map.

proj = ccrs.Mercator()

plt.figure(figsize=(10, 10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')


if __name__ == "__main__":
    plt.figure(figsize=(7, 7))
    plt.plot(x, y, "b.")
    ind = np.isnan(speed)
    plt.hist(speed[~ind], bins=np.linspace(0, 30, 20))
    plt.xlabel(" 2D speed (m/s) ")
    plt.ylabel(" Frequency ")
    plt.show()
    plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
    plt.xlabel(" Observation ")
    plt.ylabel(" Elapsed time (days) ")
    plt.show()
    plt.figure(figsize=(8, 6))
    plt.plot(daily_mean_speed, "rs-")
    plt.xlabel(" Day ")
    plt.ylabel(" Mean Speed (m/s) ");
    plt.show()
    for name in bird_names:
        ix = birddata['bird_name'] == name
        x, y = birddata.longitude[ix], birddata.latitude[ix]
        ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)
    plt.legend(loc="upper left")
    plt.show()
