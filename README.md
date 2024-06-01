# Time Series Clustering
Implemented Time Series Kmeans with Dynamic Time Warping on metereological data of Emilia-Romagna provinces.

Sum of Within cluster distances and Silhouette Score were used to choose the appropriate number of clusters.

The datasets contains Emilia Romagna metereological data collected from 2017 to 2020.
The files are for the Emilia Romagna provinces:

Bologna
Ferrara
Forlì-Cesena
Modena
Parma
Piacenza
Ravenna
Reggio Emilia
Rimini

Here's a brief explanation of some of the used meteorological columns:

- TG (Temperature of the Air): This usually represents the mean daily air temperature.

- TN (Minimum Temperature of the Air): This represents the minimum daily air temperature.

- TX (Maximum Temperature of the Air): This represents the maximum daily air temperature.

- HU (Relative Humidity): This represents the percentage of moisture in the air relative to the maximum amount the air could hold at the same temperature. It gives an indication of how "humid" or "dry" the air is.

- PP (Total Precipitation): This represents the total amount of precipitation (rain, snow, etc.) that fell during a specific period, usually in millimeters.

- QQ (Specific Humidity): Specific humidity is the ratio of the mass of water vapor to the total mass of air. It is another measure of humidity and is expressed in grams of water vapor per kilogram of air.

- RR (Precipitation Duration): This may represent the duration of precipitation, indicating the amount of time during which precipitation occurred. It is often measured in hours.
