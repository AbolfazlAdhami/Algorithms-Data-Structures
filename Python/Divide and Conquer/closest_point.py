import math
class Points:
        def __init__(self,x,y) -> None:
                self.x = x
                self.y = y
                
def distance(p,q):
        return math.sqrt((p.x-q.x)**2 + (p.y-q.y)**2)


# O(n) n^4
def brut_force(sub_array):
        min_distance=float('inf')
        
        for i in range(len(sub_array)-1):
                for j in range(i+1,len(sub_array)):
                        actual_distance=distance(sub_array[1],sub_array[2])
                        if actual_distance < min_distance:
                                min_distance=actual_distance
        return min_distance


def get_strip_delta(strip_points,delta):
        min_distance = delta
        n = len(strip_points)
        
        for i in range(n):
                j=i+1
                while j <  n and (strip_points[j].y - strip_points[i].j) <min_distance:
                        min_distance = distance(strip_points[j],strip_points[i])
                        j+=1
                        
        return min_distance

def closest_pairs_algorithm(list_sorted_x,list_sorted_y,nums_of_items):
        if nums_of_items <= 5 :
                return brut_force(list_sorted_x)
        
        middle_index=nums_of_items //2
        middle_item=list_sorted_x[middle_index]
        
        delta_left = closest_pairs_algorithm(list_sorted_x[:middle_index],list_sorted_y,middle_index)
        delta_right = closest_pairs_algorithm(list_sorted_x[middle_index:],list_sorted_y,nums_of_items-middle_index)
        
        delta=min(delta_left,delta_right)
        
        strip_points=[]
        
        
        for i in range(nums_of_items):
                if abs(list_sorted_y[i].x - middle_item.x) < delta:
                        strip_points.append(list_sorted_y[i])
                        
        strip_delta=get_strip_delta(strip_points,delta)
        
        return min(delta,strip_delta)
        
        
        
def run(list1,list2):
        list1.sort(key=lambda point: point.x)
        list2.sort(key=lambda point: point.y)
        return closest_pairs_algorithm(list1,list2,len(list1))


if __name__ == "__main__":
        points = [Points(1, 1), Points(4, 2),Points(10,10),Points(1,2),Points(5,3)]
        
        l1=list(points)
        l2=list(points)
        
        print(run(l1,l2))