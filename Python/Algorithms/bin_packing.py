def first_fit_decreasing(items, bin_capacity):
    # Sort items in decreasing order
    items.sort(reverse=True)
    
    bins = []
    
    for item in items:
        placed = False
        
        # Try to place the item in one of the existing bins
        for b in bins:
            if sum(b) + item <= bin_capacity:
                b.append(item)
                placed = True
                break
        
        # If the item was not placed in any existing bin, create a new bin
        if not placed:
            bins.append([item])
    
    return bins


def first_fit_decreasing_algorithm(capacities, bin_max_capacity):
        solution_bins = []
        
        items_names = list(capacities.keys())
        sorted_items = sorted(items_names, key=lambda x: capacities[x], reverse=True)
        print( sorted_items)
        
        for item in sorted_items:
            bin_found = False
            item_capacity = capacities[item]
            
            for index, actual_bin in enumerate(solution_bins):
                
                actual_bin_summed_size=sum([capacities[key] for key in actual_bin])
                
                if item_capacity <= (bin_max_capacity - actual_bin_summed_size):
                    solution_bins[index].append(item)
                    bin_found=True
                    break
            if not bin_found:
                solution_bins.append([item])
                
        return solution_bins
        
if __name__ == '__main__':
    items = {'item#1': 4, 'item#2': 1, 'item#3':7,'item#4':5,'item#5':6,'item#6':3}
    print(first_fit_decreasing_algorithm(items,8))