# Unreal GIS Project

## This project tries to create a digital version of the city of Kaufbeuren in Bavaria,Germany.

### Reference image
Image of the Heightmap and some major roads in QGIS.
<img width="633" height="511" alt="image" src="https://github.com/user-attachments/assets/6b2ff765-1e3c-4655-8f50-3c8061f8c23c" />



Image of the Heightmap and some major roads in Unreal Engine 5 (Only 2/5ths of the roads present).
<img width="935" height="721" alt="image" src="https://github.com/user-attachments/assets/adef7bea-acde-484c-b18d-44d23875eeba" />




On the ground view of the roads.
<img width="1194" height="428" alt="image" src="https://github.com/user-attachments/assets/0aab3545-ef63-4a08-b6bf-c78ea1b23b74" />




### Issues experienced in the process
- Finding good data was difficult. Managed to find road data from https://www.bbbike.org/ (But this includes train tracks)
- Exporting as .csv file from QGIS lead to a lot of datapoints for the roads (approx. 24.000 points), so I used a python script to remove redundant points (removed approx. 19.000 points) and made parsing in UE easier.
- I failed to export the heightmap and the roads in a way that made matching them in UE easy. I had to move the roads manually in place to get it to work.
- The exported roads are for some reason mirrored.
- Tried to look for Satellite images to map onto the heightmap, but most free images are too low resolution.
- Creating roads out of 5000 points is very computationally heavy, so only ended up using 2000 points. More optimization is needed.
- Mapping the Roads on the heightmap is not easy, some roads pierce the ground, others hover slightly above it. (UEs own landscape spline system would probably be better.)
