def distance(strand_a, strand_b):
    try:
        
        strand_a = [i for i in strand_a]
        strand_b = [i for i in strand_b]
        return len(strand_a) - len([0 for i, j in zip(strand_a, strand_b) if i == j])
    except ValueError:
        print("Error!")
        
    
