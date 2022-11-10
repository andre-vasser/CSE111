import math 

def main():
    
    name = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
    radius_list = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
    height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78 ,12.38, 11.27, 11.11]
    cost_list = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    for i in range(12):
        volume = compute_volume(radius_list[i], height_list[i])
        surface_area = compute_surface_area(radius_list[i], height_list[i])
        efficiency = compute_cost_efficiency(cost_list[i])
        print(f'{name[i]}, {volume:.2f}, {surface_area:.2f}')
        
    
def compute_cost_efficiency(radius, height, volume, cost_list ):
    volume = compute_volume(radius, height)
    efficiency = volume / cost_list
    return efficiency

def compute_volume(radius, height):
    
    volume = math.pi * (radius**2 * height) 
    return volume



def compute_surface_area(radius, height):
    
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


main()
